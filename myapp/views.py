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
title = "Craigslist, Inc."

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


class Ad():
    pass

def extract_img_links(a_tag):
    url = "https://images.craigslist.org/"
    if a_tag:
        link = a_tag["data-ids"].split(':')[1]
        link = link.split(',')[0]
        url = url + link + '_300x300.jpg'
    return url

def scrapper(search):
    scrap_url = 'https://chicago.craigslist.org/search/?query={}'
    final_url = scrap_url.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features = "lxml")
    posts = soup.find_all('li', class_ = "result-row")
    ads = []
    for post in posts:
        ad = Ad()
        ad.title = post.div.h3.text.strip()
        ad.link = post.a["href"]
        price = post.find('span', class_ = "result-price")
        ad.img_link = extract_img_links(post.find('a', class_ = "result-image gallery"))
        if price:
            ad.price = price.text
        else:
            ad.price = ''
        ads.append(ad)
    return ads

def SearchView(request):
    search = request.POST.get("search")
    models.Search.objects.create(search_text = search)
    ads = scrapper(search)

    context = {
        'title' : ' | '.join([title, search]),
        'search': search,
        'ads': ads
        }
    return render(request, 'myapp/new_search.html', context)
