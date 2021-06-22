from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models

# Create your views here.
title = "Ahsenslist, Inc."

class BaseView(generic.ListView):
    template_name = 'base.html'
    context_object_name = 'pageinfo'

    def get_queryset(self):
        content = f"Your are at {title}"
        pageinfo = {
        'title' : title,
        'content': content
        }
        return pageinfo

def SearchView(request):
    search = request.POST.get("search")
    scrap_url = 'https://chicago.craigslist.org/search/?query={}'
    final_url = scrap_url.format(quote_plus(search))
    response = requests.get(final_url)
    models.Search.objects.create(search_text = search)
    data = response.text
    soup = BeautifulSoup(data, features = "lxml")
    posts = soup.find_all('li', class_ = "result-row")
    titles = []
    links = []
    prices = []
    images = []
    for post in posts:
        titles.append(post.div.h3.text.strip())
        links.append(post.a["href"])
        price = post.find('span', class_ = "result-price")
        prices.append(price)
        print (post)


    context = {
        'title' : ' | '.join([title, search]),
        'search': search
        }
    return render(request, 'myapp/new_search.html', context)
