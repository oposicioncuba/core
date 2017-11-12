from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import (
    MeSerializer,
    LocationSerializer,
    UpdateAddressSerializer,
    OrganizationSerializer
)
from apps.core.models import Member, Location, Address, Organization


class MeViewSet(ModelViewSet):
    serializer_class = MeSerializer

    def get_queryset(self):
        return Member.objects.filter(
            user__username=self.request.user.username
        )


class LocationView(ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(
            id=self.kwargs['pk']
        ).first().get_children()


class UpdateAddressView(UpdateAPIView):
    serializer_class = UpdateAddressSerializer

    def get_queryset(self):
        return Address.objects.filter(
            member__user__username=self.request.user.username
        )


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
