from django.contrib import admin 
from .models import Book    

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):

    # list_display: Controls which fields are displayed as columns in the change list page.
    list_display = ('title', 'author', 'publication_year')

    # list_filter: Adds a right-sidebar filter box to the change list page,
    list_filter = ('publication_year', 'author')

    # search_fields: Adds a search box to the top of the change list page,
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)