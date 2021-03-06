from django.db import models

# importing external models
from apps.autor.models import Author
# Create your models here.
from django.db.models.signals import post_save

# app de terceros
from PIL import Image


from .managers import BookManager, CategoryManager


class Category(models.Model):
    name = models.CharField('nombre-categoria', max_length=20, )

    object = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField('titulo', max_length=50, )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='category_book')
    authors = models.ManyToManyField(Author)
    date = models.DateField()
    portrait = models.ImageField(upload_to='portraits/', max_length=100)
    visits = models.PositiveIntegerField()

    object = BookManager()

    def __str__(self):
        return self.title


def optimize_image(sender, instance, **kwargs):
    print(" ------- ")
    if instance.portrait:
        portrait = Image.open(instance.portrait.path)
        portrait.save(instance.portrait.path, quality=20, optimize=True)


post_save.connect(optimize_image, sender=Book)
