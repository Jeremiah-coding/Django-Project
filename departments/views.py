from django.shortcuts import get_object_or_404, render

from .models import Department


def list_departments(request):
	departments = Department.objects.all().order_by("code")
	return render(request, "departments/list.html", {"departments": departments})


def department_detail(request, department_id):
	department = get_object_or_404(Department, pk=department_id)
	courses = department.courses.all().order_by("course_code")
	return render(
		request,
		"departments/detail.html",
		{"department": department, "courses": courses},
	)
