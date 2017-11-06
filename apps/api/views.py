from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import MeSerializer, LocationSerializer
from apps.core.models import Member, Location


class MeViewSet(ModelViewSet):
    serializer_class = MeSerializer

    def get_queryset(self):
        return Member.objects.filter(
            user__username=self.request.user.username
        )


class LocationView(RetrieveAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(
            id=self.kwargs['pk']
        ).first().get_children()
