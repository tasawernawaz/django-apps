__author__ = 'Tasawer Nawaz'

from django.contrib import admin
from books.models import Author, Publisher, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    search_fields = ('title',)
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('author',)
    raw_id_fields = ('publisher',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)

