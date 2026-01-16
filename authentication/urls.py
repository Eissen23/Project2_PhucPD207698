from django.urls import path
from .views import SignupView, RetrieveUserView

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('me', RetrieveUserView.as_view()),
]