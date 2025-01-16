from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            email='test@example.com',
            role='regular'
        )

    def test_user_creation(self):
        """Test that a user creation with below attributes is successful"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.role, 'regular')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    def test_user_role_choices(self):
        """Test that user roles are limited to defined choices"""
        admin_user = get_user_model().objects.create_user(
            username='adminuser',
            password='12345',
            role='admin'
        )
        self.assertEqual(admin_user.role, 'admin')
