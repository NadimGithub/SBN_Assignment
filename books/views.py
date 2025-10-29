from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Book
from .forms import BookForm
from .serializers import BookSerializer
from rest_framework import generics
import requests

# ---------- Frontend Views ----------
def book_list(request):
    books = Book.objects.order_by('-created_at')
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Add'})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Edit'})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_detail.html', {'book': book, 'confirm_delete': True})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def dashboard(request):
    # Data for chart: count of books per author
    qs = Book.objects.values('author').order_by('author')
    data = {}
    for row in qs:
        author = row['author'] or 'Unknown'
        data[author] = Book.objects.filter(author=author).count()
    # send JSON data to template to be consumed by Chart.js
    return render(request, 'books/dashboard.html', {'chart_data': data})

# AJAX endpoint to fetch book info from OpenLibrary by ISBN
def fetch_openlibrary(request):
    isbn = request.GET.get('isbn', '').strip()
    if not isbn:
        return JsonResponse({'error': 'No ISBN provided'}, status=400)
    # OpenLibrary API: https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data
    url = f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data'
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        key = f'ISBN:{isbn}'
        if key in data:
            book = data[key]
            title = book.get('title', '')
            authors = book.get('authors', [])
            author_name = authors[0]['name'] if authors else ''
            return JsonResponse({'title': title, 'author': author_name})
        else:
            return JsonResponse({'error': 'No data found for this ISBN'}, status=404)
    except requests.RequestException:
        return JsonResponse({'error': 'Failed to fetch data from OpenLibrary'}, status=500)

# ---------- REST API Views ----------
class BookListCreateAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer

class BookRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
