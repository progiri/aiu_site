from rest_framework import routers
from django.urls import path

from .views import NewsCRUDView, NewsListView

urlpatterns = [
    path('', NewsListView.as_view()),
]

router = routers.SimpleRouter()
router.register(r'admin', NewsCRUDView)

urlpatterns += router.urls
