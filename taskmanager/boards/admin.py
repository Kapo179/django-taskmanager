"""
Django admin configuration for the boards app.
Customizes the admin interface for task and status management.
"""

from django.contrib import admin
from .models import Status, Task

admin.site.register(Status)
admin.site.register(Task)
