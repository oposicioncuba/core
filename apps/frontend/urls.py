from django.conf.urls import url, include
from django.contrib import admin

from apps.frontend.views import RedirectBasedOnCredentialsView

urlpatterns = [
    url(r'^$', RedirectBasedOnCredentialsView.as_view(), name='redirect'),
]
