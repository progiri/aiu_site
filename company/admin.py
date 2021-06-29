from django.contrib import admin
from .models import Location, Position, Company


# Register your models here.
admin.site.register(Location)
admin.site.register(Position)
admin.site.register(Company)
