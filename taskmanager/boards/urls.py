from django.urls import path
from . import views

# URL patterns for the boards app
urlpatterns = [
    # Homepage - displays the Kanban board
    path('', 
         views.board_view, 
         name='board'), 
    
    # Handle new task creation
    path('task/add/', 
         views.add_task, 
         name='add_task'),  
    
    # Handle task status updates
    path('task/<int:task_id>/update/', 
         views.update_task_status, 
         name='update_task_status'),  
] 