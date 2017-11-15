from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.api import google
from apps.core.models import Member, Address, Location, Organization


class AddressField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        geocoded_address = google.geocode(data)

        location, created = Location.objects.get_or_create(
            name=geocoded_address['country'],
            defaults={
                'name': geocoded_address['country']
            }
        )

        location, created = Location.objects.get_or_create(
            name=geocoded_address['location'],
            parent=location,
            defaults={
                'parent': location,
                'name': geocoded_address['location']
            }
        )

        address, created = Address.objects.get_or_create(
            street=geocoded_address['street'],
            number=geocoded_address['number'],
            defaults={
                'location': location
            }
        )

        return address


class AddressSerializer(ModelSerializer):
    location = SerializerMethodField()

    class Meta:
        model = Address
        fields = (
            'id',
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


class OrganizationSerializer(ModelSerializer):
    headquarter = AddressField()

    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class MeSerializer(ModelSerializer):
    address = SerializerMethodField()
    organizations = SerializerMethodField()

    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'last_name',
            'birthday',
            'address',
            'photo',
            'organizations',
        )

    def get_address(self, obj):
        address = Address.objects.filter(
            id=obj.address.id
        ).first()

        if address:
            return AddressSerializer(address).data
        else:
            return ''

    def get_organizations(self, obj):
        return OrganizationSerializer(obj.organizations.all(), many=True).data


class LocationSerializer(ModelSerializer):
    label = serializers.CharField(source='name')
    isBranch = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('id', 'label', 'isBranch',)

    def get_isBranch(self, obj):
        return not obj.is_leaf_node()


class UpdateAddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
