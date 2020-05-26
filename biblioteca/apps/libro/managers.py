from django.db import models

from django.db.models import Q, Count


class BookManager(models.Manager):
    def list_books(self):
        return self.all()

    def filter_category(self, category):
        res = self.filter(
            category__name__icontains=category,
        ).order_by('title')
        return res

    def bookPerPrestamo(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado

    def num_prestados(self):
        res = self.annotate(
            num_prestados=Count('libro_prestamo')
        )

        for r in res:
            print('---------')
            print(r, r['num_prestados'])

        return res


class CategoryManager(models.Manager):
    """ Manager for categories """

    def categoryPerAuthor(self, author):
        res = self.filter(
            category_book__authors__id=author
        ).distinct()
        return res

    def listarCategoria(self):
        res = self.annotate(
            num_libros=Count('category_book')
        )
        for r in res:
            print(r, r.num_libros)
        return res

