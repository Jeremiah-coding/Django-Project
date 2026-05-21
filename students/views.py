from django.http import JsonResponse


def list_students(_request):
	return JsonResponse(
		{
			"app": "students",
			"items": ["Alice", "Bob", "Charlie"],
		}
	)

# Create your views here.
