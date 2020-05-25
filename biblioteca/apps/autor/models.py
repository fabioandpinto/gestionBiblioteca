from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField('nombre',
                            max_length=30)
    last_name = models.CharField('apellido',
                                 max_length=30)
    country = models.CharField('pais',
                               max_length=30)
    age = models.PositiveIntegerField('edad', )

    def __str__(self):
        return self.name + ' ' + self.last_name
