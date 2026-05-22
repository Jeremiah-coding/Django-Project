from django.urls import path

from .views import course_detail, list_courses

urlpatterns = [
    path('', list_courses, name='courses-list'),
    path('<int:course_id>/', course_detail, name='course-detail'),
]
