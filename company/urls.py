from .views import CompaniesViews
from .serializers import CompanySerializer
from django.urls import path

urlpatterns = [
    path('', CompaniesViews.as_view())
]

