from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


CATEGORIES = [("Novel", "Novel"), ("Mystery", "Mystery"), ("Romance", "Romance"), ("Fantasy", "Fantasy"),
              ("Young Adult", "Young Adult"), ("Thriller", "Thriller"), ("Self-Help & Personal Growth",
                                                                         "Self-Help & Personal Growth")]


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.CharField(max_length=1500, blank=True)
    slug = models.SlugField(max_length=200, null=True)
    price = models.FloatField(default=29.99)
    image = models.ImageField(upload_to='media/')
    
    class Meta:
        verbose_name_plural = 'books'

    def str(self):
        return f'Book(title={self.title}, author={self.author}, pages={self.pages}, category={self.category}, description={self.description}, price={self.price}, image={self.image}, slug={self.slug})'
    def repr(self):
        return self.str()
    
    def get_absolute_url(self):
        return reverse('book-info', args=[self.slug])
    
    def get_all_books_by_category(self):
        return reverse('by-category', args=[self.category])
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    amount_paid = models.FloatField(null=True)
    shipping_address = models.TextField(max_length=1000, null=True)
    phone = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save
   
    def str(self):

        return 'Order - #' + str(self.id)

class OrderItem(models.Model):


    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveBigIntegerField(default=1)

    price = models.DecimalField(max_digits=8, decimal_places=2)    

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def str(self):

        return 'Order Item - #' + str(self.id)