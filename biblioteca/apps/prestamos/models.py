from django.db import models

# Create your models here.
from apps.libro.models import Book

from .managers import PrestamoManager


class Lector(models.Model):
    name = models.CharField('nombre',
                            max_length=50)
    last_name = models.CharField('apellidos',
                                 max_length=50)
    country = models.CharField('nacionalidad',
                               max_length=50)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "Lectores"


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector,
                               on_delete=models.CASCADE)
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='libro_prestamo')
    date_require = models.DateField('fecha_prestamo')
    date_return = models.DateField('fecha_devolución',
                                   blank=True,
                                   null=True)
    returned = models.BooleanField('devuelto',
                                   null=True,
                                   blank=True)

    object = PrestamoManager()

    def __str__(self):
        return self.lector.name + ' ' + self.lector.last_name + ' - ' + self.book.title
