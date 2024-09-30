from django.urls import path
from book.views import *



urlpatterns = [
    path('home/', home_page, name='home'),
    path('create-book/', create_book, name='create_book'),
    path('books-list/', book_list, name='book_list'),
    

]
