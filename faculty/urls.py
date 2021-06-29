from .views import FacultiesView, FacultyCreateAPIView, RequestToDirection
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('faculties/', FacultiesView.as_view()),
    path('faculties/add/', FacultyCreateAPIView.as_view()),
    path('faculties/directions/', RequestToDirection.as_view())
]
