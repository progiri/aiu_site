from faculty.models import Faculty
from news.models import News
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


# Create your views here.

class MainPage(GenericAPIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/index.html'

    def get(self, request):
        bachelor = Faculty.objects.filter(degree='B')
        master = Faculty.objects.filter(degree='M')
        doctor = Faculty.objects.filter(degree='D')
        news = News.objects.all().order_by('-pub_date')[:7]

        return Response({
            "bachelor": bachelor,
            "master": master,
            "doctor": doctor,
            "news": news})
