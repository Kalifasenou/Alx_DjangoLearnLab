from django.contrib import admin
from .models import Book 

# Da custom ModelAdmin class 
class BookAdmin(admin.ModelAdmin): 
    list_display = ('title', 'author', 'publication_year')

    # This adds filters to the right sidebar in the admin list view
    list_filter = ('publication_year', 'author') 

    # This adds a search box to the top of the admin list view, 
    search_fields = ('title', 'author') 