from django.urls import path
from .views import index

urlpatterns = [
    path('login', index),
    path('project_manager', index),
    path('sign_up', index),
    path ('reset-password', index),
    path('password/reset/confirm/:uid/:token', index),
    path('activate/:uid/:token', index),
    path('', index),
    
]