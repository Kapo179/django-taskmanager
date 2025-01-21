"""
Django admin configuration for the accounts app.
Customizes the admin interface for user management.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface configuration for the CustomUser model
    """
    # Add role field to the admin detail view
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    # Add role field to the user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    # Fields to display in the user list
    list_display = ('username', 'email', 'role', 'is_active')
    # Fields that can be used to filter users
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
