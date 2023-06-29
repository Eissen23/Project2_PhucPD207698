from django.urls import path
from .views import index

urlpatterns = [
    path('sign_in', index),
    path('project_manager', index),
    path('sign_up', index)
]