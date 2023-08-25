from . import views
from django.urls import path, reverse


urlpatterns = [ 

    # Store main page
    path('', views.store, name='store'),

     # Individual book
    path('book/<slug:slug>/', views.book_info, name='book-info'),

    # Individual category
    path('books/<str:category>/', views.books_by_category, name='books-by-category'),

    # Cart
    path('cart/', views.cart_summary, name='cart-summary'),

    path('add/<int:id>/', views.cart_add, name='cart-add'),

    path('delete', views.cart_delete, name='cart-delete'),

    path('update', views.cart_update, name='cart-update'),

    path('checkout/', views.checkout, name='checkout'),

    path('complete-order', views.complete_order, name='complete-order'),

    path('order-success', views.order_success, name='order-success'),

    # Account register

    path('register', views.register, name='register'),

    # Login / Logout

    path('my-login', views.my_login, name='my-login'),

    path('user-logout', views.user_logout, name='user-logout'),

    

]




