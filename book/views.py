from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from book.forms import BookForm
from book.models import Book

# Create your views here.
def home_page(request):
    return render(request, 'books/home.html')

@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.updated_by = request.user
            book.save()
            return redirect('create_book')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})