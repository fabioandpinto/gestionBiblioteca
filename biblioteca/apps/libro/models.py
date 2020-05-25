from django.db import models

# importing external models
from apps.autor.models import Author
# Create your models here.


class Category(models.Model):
    name = models.CharField('nombre-categoria', max_length=20, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField('titulo', max_length=50, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    authors = models.ManyToManyField(Author)
    date = models.DateField()
    portrait = models.ImageField(upload_to='portraits/', max_length=100)
    visits = models.PositiveIntegerField()

    def __str__(self):
        return self.title


