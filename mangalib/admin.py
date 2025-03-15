from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informations du manga', {'fields': ['title', 'author']}),
        ('Informations magasin', {'fields': ['quantity']})
    ]

    list_display = ('title','author','quantity')
    list_filter = ['author']
    search_fields = ['title']
    list_per_page = 5

