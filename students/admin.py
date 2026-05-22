from django.contrib import admin
from . import models

if hasattr(models, "Student"):
	admin.site.register(models.Student)
