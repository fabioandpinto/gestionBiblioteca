from django.db import models

from django.db.models import Q


class AuthorManager(models.Manager):
    """ Managers for the Author Model"""

    def list_authors(self):
        return self.all()

    def search_author(self, name):
        res = self.filter(
            Q(name__icontains=name) | Q(last_name__icontains=name)
        )
        return res

    def list_age(self):
        res = self.filter(
            age__gt=60,
        ).order_by('last_name')
        return res
