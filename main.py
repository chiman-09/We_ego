from geopy.geocoders import Nominatim


def Coordinate(location):
    geolocator = Nominatim(scheme='http', user_agent='Weego_Web')
    location = geolocator.geocode(location)
    lats = location.latitude
    longs = location.longitude
    return lats


x = Coordinate('Brigade Gardenia Bangalore 560078')
print(x)