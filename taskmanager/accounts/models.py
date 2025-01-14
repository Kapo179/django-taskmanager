from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    Inherits default fields: username, password, email, first_name, last_name
    role-based functionality
    """
    
    # Role field - defines user permissions level
    role = models.CharField(
        max_length=50,
        choices=[
            ('admin', 'Admin'),           # Full access to all features
            ('regular', 'Regular User'),  # Standard user access
        ],
        default='regular'  # New users are regular by default
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
