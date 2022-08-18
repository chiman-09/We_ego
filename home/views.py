from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import certifi
import os
import os.path
import ssl
import stat
import subprocess
import sys
from geopy.geocoders import Nominatim
import smtplib

STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
             | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
             | stat.S_IROTH |                stat.S_IXOTH )


def main1():
    openssl_dir, openssl_cafile = os.path.split(
        ssl.get_default_verify_paths().openssl_cafile)

    subprocess.check_call([sys.executable,
        "-E", "-s", "-m", "pip", "install", "--upgrade", "certifi"])
    import certifi
    # change working directory to the default SSL directory
    os.chdir(openssl_dir)
    relpath_to_certifi_cafile = os.path.relpath(certifi.where())

    try:
        os.remove(openssl_cafile)
    except FileNotFoundError:
        pass
    #print(" -- creating symlink to certifi certificate bundle")
    os.symlink(relpath_to_certifi_cafile, openssl_cafile)
    #print(" -- setting permissions")
    os.chmod(openssl_cafile, STAT_0o775)
    #print(" -- update complete")
if __name__ == '__main__':
    main1()


def Coordinate(location):
    geolocator = Nominatim(scheme='http', user_agent='Weego_Web')
    location = geolocator.geocode(location)
    lats = location.latitude
    longs = location.longitude
    return lats


def register(request):
     return render(request, 'Weego_register.html')


def index(request):
    if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email'):
        user = User()
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.vehicle = request.POST.get('vehicle')
        user.year = request.POST.get('year')
        user.phone = request.POST.get('phone')
        user.email = request.POST.get('email')
        user.srn_number = request.POST.get('srn_number')
        user.street_address = request.POST.get('street_address')
        user.street_address2 = request.POST.get('street_address2')
        user.city = request.POST.get('city')
        user.pin_code = request.POST.get('pin_code')
        geolocator = Nominatim(scheme='http', user_agent='Weego_Web')
        ladd1 = user.street_address + ' ' + user.city + ' ' + user.pin_code
        location = geolocator.geocode(ladd1)
        user.lat = location.latitude
        user.long = location.longitude
        user.save()

    return render(request, "home.html")


def home(request):
    message = request.POST.get('Message')
    server = smtplib.SMTP_SSL("smtp@gmail.com",379)
    server.login("achintyakrishna2021@gmail.com","krishna2003")
    server.sendmail("achintyakrishna2021@gmail.com","achikrish5@gmail.com",message)
    server.quit()
    return render(request, "home.html")


def search(request):

    return render(request, "search.html")


def search_user(request):
    location = request.POST.get('search')
    lats = str(Coordinate(location))

    data = User.objects.raw(f'select * from home_user where lat between {lats} - 0.5 and {lats} + 0.5')
    use = {
        "id": data
    }
    return render(request,"search_result.html",use)





