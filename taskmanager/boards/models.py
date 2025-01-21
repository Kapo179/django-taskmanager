"""
This module defines models for the boards app.
It includes models for tasks and statuses.
"""

from django.db import models
from django.conf import settings

class Status(models.Model):
    """
    Model representing a status column on the Kanban board.
    
    Each Status represents a column that tasks can be placed in,
    such as "To Do", "In Progress", or "Done".
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return string representation of the status."""
        return self.name

    class Meta:
        """Meta options for Status model."""
        verbose_name_plural = "Statuses"

    @classmethod
    def ensure_default_statuses(cls):
        """Ensure the default statuses exist"""
        default_statuses = ['not-started', 'doing', 'done']
        for status_name in default_statuses:
            cls.objects.get_or_create(name=status_name)


class Task(models.Model):
    """
    Model representing a task in the Kanban board.
    
    Each task has a title, description, status, assigned user,
    and timestamps for creation and updates.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return string representation of the task."""
        return self.title
