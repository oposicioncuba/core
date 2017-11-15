import googlemaps
from django.conf import settings


def find_item(geocoded, lookup_field):
    for address_component in geocoded:
        if lookup_field in address_component['types']:
            return address_component['long_name']

    return ''


def geocode(address):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    geocoded = gmaps.geocode(address)[0]['address_components']

    search_dict = {
        'number': 'street_number',
        'street': 'route',
        'location': 'locality',
        'country': 'country'
    }

    result = {}

    for attr, lookup_field in search_dict.items():
        result[attr] = find_item(geocoded, lookup_field)

    return result
