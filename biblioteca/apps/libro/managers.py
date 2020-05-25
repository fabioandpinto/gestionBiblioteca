from django.db import models

from django.db.models import Q


class BookManager(models.Manager):
    def list_books(self):
        return self.all()

    def filter_category(self, category):
        res = self.filter(
            category__name__icontains=category,
        ).order_by('title')
        return res
