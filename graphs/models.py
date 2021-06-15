from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    date_reported = models.IntegerField()
    country_code = models.TextField()
    country = models.TextField()
    who_region = models.TextField()
    new_cases = models.IntegerField()
    cumulative_cases = models.IntegerField()
    new_deaths = models.IntegerField()
