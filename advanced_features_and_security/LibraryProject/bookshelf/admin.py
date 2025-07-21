from django.contrib import admin 
from .models import Book      
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class BookAdmin(admin.ModelAdmin):

    # list_display: Controls which fields are displayed as columns in the change list page.
    list_display = ('title', 'author', 'publication_year')

    # list_filter: Adds a right-sidebar filter box to the change list page,
    list_filter = ('publication_year', 'author')

    # search_fields: Adds a search box to the top of the change list page,
    search_fields = ('title', 'author')



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin, Book, BookAdmin)