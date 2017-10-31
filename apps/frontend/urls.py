from django.conf.urls import url

from apps.frontend.views import RedirectBasedOnCredentialsView, ProfileView

urlpatterns = [
    url(r'^$', RedirectBasedOnCredentialsView.as_view(), name='redirect'),
    url(r'^accounts/profile/', ProfileView.as_view(), name='profile'),
]
