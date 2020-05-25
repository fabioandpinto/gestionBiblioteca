from django.shortcuts import render

from django.views.generic import ListView


# Create your views here.
from apps.autor.models import Author


class ListAutores(ListView):
    context_object_name = 'author_list'
    template_name = "autor/lista.html"

    def get_queryset(self):
        kword = self.request.GET.get('name', '')
        return Author.object.search_author(kword)