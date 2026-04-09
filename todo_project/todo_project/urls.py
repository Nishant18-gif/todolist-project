"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# ----------------------------
# Custom error handlers
# ----------------------------
def custom_404(request, exception):
    return JsonResponse({
        "status": False,
        "code": 404,
        "message": "URL not found"
    }, status=404)

def custom_403(request, exception):
    return JsonResponse({
        "status": False,
        "code": 403,
        "message": "Permission denied"
    }, status=403)

def custom_500(request):
    return JsonResponse({
        "status": False,
        "code": 500,
        "message": "Internal server error"
    }, status=500)

def custom_400(request, exception):
    return JsonResponse({
        "status": False,
        "code": 400,
        "message": "Bad request"
    }, status=400)

# ----------------------------
# URL patterns
# ----------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('auth/', include('auth_app.urls')),
]

# ----------------------------
# Assign handlers
# ----------------------------
handler404 = custom_404
handler403 = custom_403
handler500 = custom_500
handler400 = custom_400
