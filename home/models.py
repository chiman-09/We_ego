from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=9663823455)
    srn_number = models.CharField(max_length=12, default="")
    vehicle = models.CharField(max_length=255, default="")
    year = models.CharField(max_length=255, default="")
    street_address = models.CharField(max_length=255, default="")
    street_address2 = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    pin_code = models.CharField(max_length=6, default="")
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)


def __str__(self):
    return self.first_name








