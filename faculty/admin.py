from django.contrib import admin
from .models import ApplicationForDirection, Faculty, SpecialDirection


# Register your models here.
admin.site.register(Faculty)
admin.site.register(SpecialDirection)
admin.site.register(ApplicationForDirection)
