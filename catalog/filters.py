import django_filters

from .models import Book


class BooksFilter(django_filters.FilterSet):
    FILTER_CHOICES = (
        ('title', 'Title (ascending)'),
        ('-title', 'Title (descending)'),
        ('-author', 'Author (descending)'),
        ('author', 'Author (ascending)'),
        ('language', 'Language (descending)'),
        ('-language', 'Language (ascending)'),
    )

    ordering = django_filters.ChoiceFilter(label="Order by", choices=FILTER_CHOICES, method="get_order_by")

    def get_order_by(self, queryset, name, value):
            return queryset.order_by(value)

    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'genre__name': ['icontains'],
            'isbn': ['icontains'],
            'author': ['exact'],
            'language':['exact'],
        }

