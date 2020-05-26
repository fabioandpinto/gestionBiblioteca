from django.db import models

from django.db.models import Q, Count, Avg


class PrestamoManager(models.Manager):
    """ procedures for prestamos"""

    def promedioEdades(self):
        res = self.filter(
            book__id='4'
        ).aggregate(
            avg_edad=Avg('lector__age'),
            sum_edad=Avg('lector__age')
        )
        return res

    def num_prestados(self):
        res = self.values(
            'book'
        ).annotate(
            num_prestados=Count('book')
        )

        for r in res:
            print('---------')
            print(r, r['num_prestados'])

        return res