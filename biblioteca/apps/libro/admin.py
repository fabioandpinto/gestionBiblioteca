from django.contrib import admin

from .models import Category, Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    list_display = (
        'title',
        'category',
    )


admin.site.register(Category)
admin.site.register(Book, BookAdmin)