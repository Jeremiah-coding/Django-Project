from django.urls import path

from .views import department_detail, list_departments

urlpatterns = [
    path('', list_departments, name='departments-list'),
    path('<int:department_id>/', department_detail, name='department-detail'),
]
