from django.http import JsonResponse
from .models import Task
from auth_app.models import UserToken
from django.views.decorators.csrf import csrf_exempt


# Show tasks for logged-in user via token
def task_list(request):
    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({"error": "Token required"})

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user
        tasks = Task.objects.filter(user=user).values()
        return JsonResponse(list(tasks), safe=False)

    except UserToken.DoesNotExist:
        return JsonResponse({"error": "Invalid token"})


# Add task via token
@csrf_exempt
def add_task(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required"})

    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({"error": "Token required"})

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        title = request.POST.get("title")
        if not title:
            return JsonResponse({"error": "Title is required"})

        Task.objects.create(title=title, user=user)

        return JsonResponse({"message": "Task added"})

    except UserToken.DoesNotExist:
        return JsonResponse({"error": "Invalid token"})


# Delete task via token
@csrf_exempt
def delete_task(request, task_id):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required"})

    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({"error": "Token required"})

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        Task.objects.filter(id=task_id, user=user).delete()

        return JsonResponse({"message": "Task deleted"})

    except UserToken.DoesNotExist:
        return JsonResponse({"error": "Invalid token"})


# Update task via token
@csrf_exempt
def update_task(request, task_id):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required"})

    token_key = request.headers.get('Authorization')
    if not token_key:
        return JsonResponse({"error": "Token required"})

    try:
        token = token_key.split(" ")[1]
        user = UserToken.objects.get(token=token).user

        task = Task.objects.get(id=task_id, user=user)

        new_title = request.POST.get("title")
        completed = request.POST.get("completed")

        if new_title:
            task.title = new_title

        if completed is not None:
            task.completed = completed.lower() == "true"

        task.save()

        return JsonResponse({"message": "Task updated"})

    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"})

    except UserToken.DoesNotExist:
        return JsonResponse({"error": "Invalid token"})