from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.api.views import MeViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'me', MeViewSet, base_name='me')
router.register(r'locations', LocationViewSet, base_name='locations')


urlpatterns = [
    url(r'^', include(router.urls)),
]
