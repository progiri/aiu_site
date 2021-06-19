from rest_framework import routers
from django.urls import path

from .views import NewsView, NotificationsView

urlpatterns = [
    path('notifications', NotificationsView.as_view())
]

router = routers.SimpleRouter()
router.register(r'', NewsView)

urlpatterns += router.urls
