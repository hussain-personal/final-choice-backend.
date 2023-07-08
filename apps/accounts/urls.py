from django.urls import path
from django.http import JsonResponse
from . import views


def index(request):
    return JsonResponse("accounts", safe=False)


urlpatterns = [
    path("", index),
    path("auth-signup/", views.SignUp.as_view()),
    path("auth-validate-email/", views.validte_email),
    path("auth-validate-username/", views.validte_username),
]
