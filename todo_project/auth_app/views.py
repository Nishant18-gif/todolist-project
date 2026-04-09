from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, UserToken


# Signup API
@csrf_exempt
def signup(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "code": 400,
            "message": "User already exists"
        })

    user = User.objects.create(username=username, password=password)

    return JsonResponse({
        "status": True,
        "code": 200,
        "message": "Signup successful"
    })


# Login API with custom token
@csrf_exempt
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    try:
        user = User.objects.get(username=username)

        if user.password == password:

            token_obj, created = UserToken.objects.get_or_create(user=user)

            return JsonResponse({
                "status": True,
                "code": 200,
                "message": "Login successful",
                "token": token_obj.token
            })

        return JsonResponse({
            "status": False,
            "code": 401,
            "message": "Invalid password"
        })

    except User.DoesNotExist:
        return JsonResponse({
            "status": False,
            "code": 404,
            "message": "User not found"
        })