"""
This module contains tests for the views in the boards app.
It includes tests for the board view, task creation, and task deletion.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from boards.models import Task, Status

class BoardViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()

        # this creates a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.client.login(username='testuser', password='12345')

        # this creates a default status
        self.status = Status.objects.create(name="To Do")

    def test_board_view_authenticated(self):
        """This ensures the board view returns a 200 for logged-in users."""
        url = reverse('board')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'boards/board.html')

    def test_board_view_anonymous_redirect(self):
        """Ensures non-logged in users are redirected to login."""
        self.client.logout()  # simulate a non-logged in user
        url = reverse('board')
        response = self.client.get(url)
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_add_task(self):
        """POST request with valid data should create a new Task."""
        url = reverse('add_task')
        form_data = {
            'title': 'Unit Test Task',
            'description': 'Test add_task view',
            'status': self.status.id,
        }
        response = self.client.post(url, form_data)
        # Should redirect back to 'board' after creation
        self.assertRedirects(response, reverse('board'))

        # Check the task was created
        self.assertTrue(Task.objects.filter(title='Unit Test Task').exists())
