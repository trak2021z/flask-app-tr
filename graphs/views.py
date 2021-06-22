import time

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from .models import Data
from datetime import datetime
import requests

def upload_data(request):
    data_url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
    req = requests.get(data_url)
    url_content = req.content.decode()
    records = url_content.split("\n").__iter__()
    records.__next__()

    for record in records:
        record_elems = record.split(',')
        date = int(datetime.strptime(record_elems[0], '%Y-%m-%d').timestamp())
        country_code = record_elems[1]
        country = record_elems[2]
        who_region = record_elems[3]
        new_cases = int(record_elems[4])
        cumulative_cases = int(record_elems[5])
        new_deaths = int(record_elems[6])
        cumulative_deaths = int(record_elems[7])
        new_data = Data(date_reported=date, country_code=country_code, country=country, who_region=who_region,
                        new_cases=new_cases, cumulative_cases=cumulative_cases, new_deaths=new_deaths,
                        cumulative_deaths=cumulative_deaths)
        new_data.save()


def showDataForCountry(request, countryCd='PL'):
    if request.method == 'GET':
        data_for_country = Data.objects.all().filter(country_code=countryCd).order_by('date_reported')
    return render(request, "DataForCountry.html", {'data_for_country': data_for_country})

def data_chart(request, countryCd='PL'):
    labels = []
    data = []
    if request.method == 'GET':
        data_for_country = Data.objects.all().filter(country_code=countryCd).order_by('date_reported')
        for el in data_for_country:
            data.append(el.cumulative_cases)
            labels.append(time.strftime('%Y-%m-%d', time.localtime(el.date_reported)))

    return render(request, "DataChart.html", {'labels': labels, 'data': data})
