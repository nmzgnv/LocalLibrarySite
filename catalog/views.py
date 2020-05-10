from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a') #available
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_books_with_word = Book.objects.filter(title__icontains = "ВИй").count()

    return render(
        request, 'index.html',
        context = {'num_books': num_books, 'num_instances': num_instances,
                   'num_instances_available': num_instances_available, 'num_authors': num_authors,
                   "num_genres": num_genres, "num_books_with_word": num_books_with_word, },
    )


class BookListView(generic.ListView):
    paginate_by = 10
    model = Book
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    paginate_by = 10
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
