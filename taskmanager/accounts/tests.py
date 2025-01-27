"""
This module contains tests for the accounts app.
It includes tests for user authentication and user management.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountTests(TestCase):
    """Test cases for account functionality including login and signup."""

    def setUp(self):
        """Set up test data including test client and user."""
        self.client = Client()
        self.user_model = get_user_model()
        # This creates a test user
        self.test_user = self.user_model.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_page(self):
        """Test that login page loads correctly"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_success(self):
        """Test successful login"""

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        }, follow=True)
        self.assertRedirects(response, reverse('board'))

    def test_login_failure(self):
        """Test login with wrong credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        """Test that signup page loads correctly"""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_success(self):
        """Test successful user registration"""
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertRedirects(response, reverse('board'))
        self.assertTrue(
            self.user_model.objects.filter(username='newuser').exists()
        )
