from django.http import JsonResponse


def list_courses(_request):
	return JsonResponse(
		{
			"app": "courses",
			"items": ["Math 101", "Chemistry 201", "Literature 150"],
		}
	)

# Create your views here.
