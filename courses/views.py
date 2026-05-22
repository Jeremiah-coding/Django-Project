from django.shortcuts import get_object_or_404, redirect, render

from .models import Course


def list_courses(request):
	first_course = Course.objects.order_by("course_code").first()
	if first_course:
		return redirect("course-detail", course_id=first_course.id)
	return redirect("departments-list")


def course_detail(request, course_id):
	course = get_object_or_404(Course.objects.select_related("department"), pk=course_id)
	return render(request, "courses/course_detail.html", {"course": course})
