from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import MeSerializer
from apps.core.models import Member


class MeViewSet(ModelViewSet):
    serializer_class = MeSerializer

    def get_queryset(self):
        return Member.objects.filter(
            user__username=self.request.user.username
        )
