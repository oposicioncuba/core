from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.api.views import MeViewSet, LocationView, UpdateAddressView

router = DefaultRouter()
router.register(r'me', MeViewSet, base_name='me')


urlpatterns = [
    url(r'^me/(?P<pk>\d+)/address/', UpdateAddressView.as_view()),
    url(r'^locations/(?P<pk>\d+)', LocationView.as_view()),
    url(r'^', include(router.urls)),
]
