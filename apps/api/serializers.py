from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.core.models import Member, Address, Location


class AddressSerializer(ModelSerializer):
    location = SerializerMethodField()

    class Meta:
        model = Address
        fields = (
            'street',
            'number',
            'additional_street',
            'location',
        )

    def get_location(self, obj):
        location = Location.objects.filter(
            id=obj.location.id
        ).first()

        if location:
            return str(location)
        else:
            return ''


class MeSerializer(ModelSerializer):
    address = SerializerMethodField()

    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'last_name',
            'birthday',
            'address',
            'photo',
        )

    def get_address(self, obj):
        address = Address.objects.filter(
            id=obj.address.id
        ).first()

        if address:
            return AddressSerializer(address).data
        else:
            return ''