from django.test import TestCase
from django.contrib.auth import get_user_model
from boards.models import Task, Status

class TaskModelTest(TestCase):
    def setUp(self):
        # this creates a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        # this creates a default status
        self.status = Status.objects.create(name="To Do")

    def test_task_creation(self):
        task = Task.objects.create(
            title="My Test Task",
            status=self.status,
            user=self.user
        )
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "My Test Task")

    def test_string_representation(self):
        task = Task.objects.create(
            title="Another Test Task",
            status=self.status,
            user=self.user
        )
        self.assertEqual(str(task), "Another Test Task")
