from django.urls import path

from .views import list_departments

urlpatterns = [
    path('', list_departments, name='departments-list'),
]
