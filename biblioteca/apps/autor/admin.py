from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('country', )
    list_display = (
        'name',
        'last_name',
        'age',
        'country',
    )


# Register your models here.
admin.site.register(Author, AuthorAdmin)