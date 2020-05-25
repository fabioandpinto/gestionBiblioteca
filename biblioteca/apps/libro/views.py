from django.views.generic import ListView

from django.shortcuts import render
from .models import Category, Book


# Create your views here.
class ListBooks(ListView):
    context_object_name = 'books'
    template_name = "book/list_books.html"

    def get_queryset(self):
        kword = self.request.GET.get('name', '')
        return Book.object.filter_category(kword)