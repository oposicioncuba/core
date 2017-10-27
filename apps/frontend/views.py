from django.urls import reverse
from django.views.generic import RedirectView


class RedirectBasedOnCredentialsView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user and self.request.user.is_authenticated:
            return reverse('profile')
        else:
            return reverse('account_login')
