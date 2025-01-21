"""
This module contains views for user authentication and user management.
It includes views for user signup and login.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    """
    Handle user signup requests.
    
    If POST request, validate form data and create new user.
    If GET request, display empty signup form.
    
    Args:
        request: The HTTP request object
        
    Returns:
        On POST with valid data: Redirect to board view
        Otherwise: Render signup form
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
