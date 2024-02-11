from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

from websitescraper_app.models import Links

# Create your views here.
def home(request):
    if request.method == "POST":
        link_new = request.POST.get('page','')
        urls = requests.get(link_new)
        print('byyyy',urls.status_code)
        bs = BeautifulSoup(urls.text,'html.parser')
        for i in bs.find_all('a'):
            li_address = i.get('href')
            li_name = i.string
            Links.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values = Links.objects.all()

        #address.append((i.get('href')))
    return render(request,'home.html',{'data_values':data_values})