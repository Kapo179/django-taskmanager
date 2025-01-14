from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Status
from django.contrib import messages

@login_required  # Ensures user is authenticated before accessing any boards
def board_view(request):
    """
    Main view for the Kanban board.
    Displays all tasks organized by their status.
    """
    # Get all statuses and their associated tasks
    statuses = Status.objects.all()
    tasks_by_status = {}
    # Organise tasks by their status 
    for status in statuses:
        tasks_by_status[status] = Task.objects.filter(
            status=status,
            user=request.user
        )
    
    return render(request, 'boards/board.html', {
        'tasks_by_status': tasks_by_status
    })

@login_required
def add_task(request):
    """Handle new task creation"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status_id = request.POST.get('status')
        # Create task only if required fields are provided
        if title and status_id:
            status = get_object_or_404(Status, id=status_id)
            Task.objects.create(
                title=title,
                description=description,
                status=status,
                user=request.user
            )
            messages.success(request, 'Task created successfully!')
        
    return redirect('board')

@login_required
def update_task_status(request, task_id):
    """Update a task's status"""
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        new_status_id = request.POST.get('status')
        # Ensure task belongs to current user
        if new_status_id:
            status = get_object_or_404(Status, id=new_status_id)
            task.status = status
            task.save()
            messages.success(request, 'Task updated successfully!')
    
    return redirect('board')
 