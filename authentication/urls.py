from django.urls import path
from .views import SignupView, RetrieveUserView, CustomLoginView, ProfileCreateView

urlpatterns = [
    path('sign-up', SignupView.as_view()),
    path('login', CustomLoginView.as_view()),
    path('me', RetrieveUserView.as_view()),
    path('info', ProfileCreateView.as_view()),
]