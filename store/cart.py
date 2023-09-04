from decimal import Decimal
from . models import Book

class Cart():

    def __init__(self, request):
        
        self.session = request.session

        # Returning user - obtain his/her existing session

        cart = self.session.get('session_key')


        # New user - generate a new session

        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}


        self.cart = cart


    def add(self, book, book_qty):

        book_id = str(book.id)


        if book_id in self.cart:

            self.cart[book_id]['qty'] = book_qty

        else:

            self.cart[book_id] = {'price': str(book.price), 'qty': book_qty}


        self.session.modified = True



    def delete(self, book):

        book_id = str(book)

        if book_id in self.cart:

            del self.cart[book_id]

        self.session.modified = True



    def update(self, book, qty):

        book_id = str(book)
        book_quantity = qty

        if book_id in self.cart:

            self.cart[book_id]['qty'] = book_quantity

        self.session.modified = True


    def __len__(self):

        return sum(item['qty'] for item in self.cart.values())



    def __iter__(self):

        all_book_ids = self.cart.keys()

        books = Book.objects.filter(id__in=all_book_ids)

        cart = self.cart.copy()

        for book in books:

            cart[str(book.id)]['book'] = book

        for item in cart.values():

            item['price'] = Decimal(item['price'])

            item['total'] = item['price'] * item['qty']

            yield item    


    
    def get_total(self):

        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())