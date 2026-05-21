from django.http import JsonResponse


def list_departments(_request):
	return JsonResponse(
		{
			"app": "departments",
			"items": ["Engineering", "Business", "Arts"],
		}
	)

# Create your views here.
