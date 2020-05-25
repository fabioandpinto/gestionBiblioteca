from django.db import models


# managers of the models
from .managers import AuthorManager


class Author(models.Model):
    name = models.CharField('nombre',
                            max_length=30)
    last_name = models.CharField('apellido',
                                 max_length=30)
    country = models.CharField('pais',
                               max_length=30)
    age = models.PositiveIntegerField('edad', )

    object = AuthorManager()

    def __str__(self):
        return self.name + ' ' + self.last_name
