from django.http import JsonResponse
from .models import Task
from auth_app.models import UserToken
from django.views.decorators.csrf import csrf_exempt


# Show tasks for logged-in user via token with optional status filter
def task_list(request):
    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Token required"
        })

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        tasks = Task.objects.filter(user=user)

        # Optional filter by status: completed / incomplete
        status_filter = request.GET.get("status")
        if status_filter == "completed":
            tasks = tasks.filter(completed=True)
        elif status_filter == "incomplete":
            tasks = tasks.filter(completed=False)

        # ✅ priority filter (NEW)
        priority_filter = request.GET.get("priority", "").lower()
        if priority_filter in ["high", "medium", "low"]:
           tasks = tasks.filter(priority=priority_filter)    

        return JsonResponse({
            "status": True,
            "code": 200,
            "message": "Tasks fetched",
            "tasks": list(tasks.values())
        })

    except UserToken.DoesNotExist:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Invalid token"
        })


# Add task via token
@csrf_exempt
def add_task(request):
    if request.method != "POST":
        return JsonResponse({
            "status": False,
            "code": 405,
            "message": "POST request required"
        })

    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Token required"
        })

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        title = request.POST.get("title")
        priority = request.POST.get("priority", "medium")
        if not title:
            return JsonResponse({
                "status": False,
                "code": 400,
                "message": "Title is required"
            })

        Task.objects.create(title=title, user=user , priority=priority)

        return JsonResponse({
            "status": True,
            "code": 200,
            "message": "Task added"
        })

    except UserToken.DoesNotExist:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Invalid token"
        })


# Delete task via token
@csrf_exempt
def delete_task(request, task_id):
    if request.method != "POST":
        return JsonResponse({
            "status": False,
            "code": 405,
            "message": "POST request required"
        })

    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Token required"
        })

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        Task.objects.filter(id=task_id, user=user).delete()

        return JsonResponse({
            "status": True,
            "code": 200,
            "message": "Task deleted"
        })

    except UserToken.DoesNotExist:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Invalid token"
        })


# Update task via token (title + completed toggle)
@csrf_exempt
def update_task(request, task_id):
    if request.method != "POST":
        return JsonResponse({
            "status": False,
            "code": 405,
            "message": "POST request required"
        })

    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Token required"
        })

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        task = Task.objects.get(id=task_id, user=user)

        new_title = request.POST.get("title")
        completed = request.POST.get("completed")

        if new_title:
            task.title = new_title

        if completed is not None:
            # Convert string "true"/"false" to boolean
            task.completed = completed.lower() == "true"

        task.save()

        return JsonResponse({
            "status": True,
            "code": 200,
            "message": "Task updated"
        })

    except Task.DoesNotExist:
        return JsonResponse({
            "status": False,
            "code": 404,
            "message": "Task not found"
        })

    except UserToken.DoesNotExist:
        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Invalid token"
        })