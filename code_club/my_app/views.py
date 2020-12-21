import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
# from requests.compat import quote_plus
from django.shortcuts import render
from . import models

# Create your views here.

BASE_CRAIGLIST_URL = 'https://delhi.craigslist.org/d/services/search/bbb?query={}'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    # print(quote_plus(search))
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('a', {'class': 'result-title'})
    print(post_titles)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
