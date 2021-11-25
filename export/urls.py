from django.urls import path

from .views import ExportViews

urlpatterns = [
    path('', ExportViews.as_view())
]
