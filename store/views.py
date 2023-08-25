from django.shortcuts import get_object_or_404, render, redirect
from . models import Book, User, Order, OrderItem
from . cart import Cart
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def store(request):
    book_list = Book.objects.all()
    context = {'books': book_list}
    return render(request, 'store/store.html', context)

def books_by_category(request, category):
    books = Book.objects.filter(category=category)
    context = {'books': books}
    return render(request, 'store/store.html', context)
    
def book_info(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {'book': book}
    return render(request, 'store/book-info.html', context)

def cart_summary(request):

    cart = Cart(request)
    context = {'cart':cart}
    return render(request, 'store/cart-summary.html', context)

@ensure_csrf_cookie
def cart_add(request, id):
    
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        book_id = int(request.POST.get('book_id'))
        book_quantity = int(request.POST.get('book_quantity'))
        book = Book.objects.get(id=book_id)
        cart.add(book=book, book_qty=book_quantity)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response

@ensure_csrf_cookie
def cart_delete(request):
    
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        book_id = int(request.POST.get('book_id'))

        cart.delete(book=book_id)


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})

        return response
    
@ensure_csrf_cookie
def cart_update(request):
    
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        book_id = int(request.POST.get('book_id'))
        book_quantity = int(request.POST.get('book_quantity'))
        book = Book.objects.get(id=book_id)
        
        cart.update(book=book_id, qty=book_quantity)


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})

        return response

def checkout(request):

    if request.user.is_authenticated:
        full_name = User.objects.get(user=request.user.id)
        context = {'name': full_name}
        return render(request, 'store/checkout.html', context)
    
    else:
        return render(request, 'store/checkout.html')

@ensure_csrf_cookie
def complete_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')

        shipping_address = (f"{address} {country} {city} {zipcode}")

        cart = Cart(request)

        total_cost = cart.get_total()

        order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address)
        
        amount_paid = total_cost

        order_id = order.pk

        for item in cart:

            OrderItem.objects.create(order_id=order_id, book=item['book'], quantity=item['qty'], price=item['price'])

        order_success = True    

        response = JsonResponse({'success':order_success})

        return response
    

def order_success(request):

    for key in list(request.session.keys()):
        if key ==  'session_key':
            del request.session[key]

    return render(request, 'store/order-success.html')

def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store/my-login.html')
    
    context = {'form':form}
    

    return render(request, 'store/register.html', context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("store")
            
    context = {'form':form}

    return render(request, 'store/my-login.html', context)

def user_logout(request):
    auth.logout(request)
    return redirect("store")
            







        



    
        
