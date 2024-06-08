from django.urls import path

from . import views

urlpatterns = [
    path('signUp/', views.user_signup)
]
