from django.db import models
from django.conf import settings

class Status(models.Model):
    # Stores the different columns of the Kanban board (e.g., "To Do", "In Progress", "Done")
    name = models.CharField(max_length=50)

    def __str__(self):
        # Display the status name in admin panel and shell
        return self.name

    class Meta:
        verbose_name_plural = "Statuses"  # Fix plural form in admin panel


class Task(models.Model):
    # Task information section
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # Relationships section
    status = models.ForeignKey(Status, on_delete=models.CASCADE)  # Which column the task belongs to
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Changed from User to settings.AUTH_USER_MODEL
        on_delete=models.CASCADE
    )
    
    # Timestamps section
    created_at = models.DateTimeField(auto_now_add=True)  # When task was created
    updated_at = models.DateTimeField(auto_now=True)      # When task was last modified

    def __str__(self):
        # Display the task title in admin panel and shell
        return self.title
