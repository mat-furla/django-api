from django.urls import path
from .views import UserViews

urlpatterns = [
    path('users/', UserViews.as_view()),
    path('users/<str:id>', UserViews.as_view())
]
