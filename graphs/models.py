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
    cumulative_deaths = models.IntegerField()


class History(models.Model):
    id_customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_customer')
    country_Cd = models.TextField()
    valid_from = models.IntegerField()
    valid_to = models.IntegerField()
    function = models.TextField()
    fit_perctentage = models.TextField()
