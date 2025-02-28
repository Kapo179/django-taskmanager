from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Status, TaskUpdate
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone


@login_required  # Ensures user is authenticated before accessing any boards
def board_view(request):
    """
    Main view for the Kanban board.
    Displays all tasks organized by their status.
    """
    # Get all tasks for the current user
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'boards/board.html', {
        'tasks': tasks  # tasks rendered in the board.html template
    })


@login_required
def add_task(request):
    """Handle new task creation"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status_name = request.POST.get('status')
        duedate = request.POST.get('duedate')
        tag = request.POST.get('tag')  # Get the tag value from the form

        # Create task only if required fields are provided
        if title and status_name:
            status = Status.objects.get_or_create(name=status_name)[0]
            Task.objects.create(
                title=title,
                description=description,
                status=status,
                user=request.user,
                duedate=duedate if duedate else None,
                # Set the tag, defaulting to empty string if not provided
                tag=tag if tag else ''
            )
            messages.success(request, 'Task created successfully!')
    return redirect('board')


@login_required
def update_task_status(request, task_id):
    """Update a task's status"""
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)

        # Handle status update
        new_status_name = request.POST.get('status')

        if new_status_name:
            # This checks, to ensure we have the status in our database
            status = Status.objects.filter(name=new_status_name).first()
            if not status:
                # Create the status if it doesn't exist
                status = Status.objects.create(name=new_status_name)

            task.status = status

        # Handle other field updates
        if 'duedate' in request.POST:
            task.duedate = request.POST.get('duedate') or None
        if 'title' in request.POST:
            task.title = request.POST.get('title')
        if 'description' in request.POST:
            task.description = request.POST.get('description')

        task.save()
        messages.success(request, 'Task updated successfully!')

    return redirect('board')


@login_required
def delete_task(request, task_id):
    """Delete a task"""
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    return redirect('board')


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'boards/task_detail.html', {'task': task})


@login_required
def add_task_update(request, task_id):
    """Add an update/comment to a task"""
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        content = request.POST.get('content')
        
        if content:
            update = TaskUpdate.objects.create(
                task=task,
                content=content
            )
            # Return JSON response for AJAX request
            return JsonResponse({
                'status': 'success',
                'created_at': timezone.localtime(update.created_at).strftime("%b %d, %Y %H:%M")
            })
        
    # Return error response if something went wrong
    return JsonResponse({'status': 'error'}, status=400)
