from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.api.views import MeViewSet

router = DefaultRouter()
router.register(r'me', MeViewSet, base_name='me')


urlpatterns = [
    url(r'^', include(router.urls)),
]
