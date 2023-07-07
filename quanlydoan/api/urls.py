from django.urls import path
from .views import SignupvView, RetrieveUserView

urlpatterns = [
    path('signup', SignupvView.as_view()),
    path('me', RetrieveUserView.as_view()),
]