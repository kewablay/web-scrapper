from django.shortcuts import render
import requests 
from bs4 import BeautifulSoup
from . import models 

# Create your views here.
ALIBABA_URL = 'https://www.alibaba.com//trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={}'

EBAY_URL = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=iphone+&_sacat=0'

def index(request):
    return render(request, "index.html")

def new_search(request):
    response = requests.get(EBAY_URL)
    data = response.text 
    soup = BeautifulSoup(data, features="html.parser")
    ebay_item_list = soup.find_all(class_ = 's-item')
    print(len(ebay_item_list))
    # another_item_list = ebay_item_list.find_all('h3')
    for products in ebay_item_list: 
        ebay_item_name = products.find('h3').text
        ebay_item_price = products.find('span', class_ = 's-item__price')
        for price in ebay_item_price:
            actual_price = price.find('span').text
            print(actual_price)

    # ---------- EBAY ITEMS TO SCRAPE -------------
    # for items in ebay_item_list:
        # ebay_item_name = soup.find(class_ = 's-item__title').text
        # ebay_item_name = soup.find(class_ = 's-item s-item__sep-on-bottom').find('h3').text
        # print(ebay_item_name)
        # ebay_item_price = soup.find(class_ = 's-item__price').text
        # print(ebay_item_price)
        # ebay_item_url = soup.find_all(class_ = 's-item s-item__sep-on-bottom').find('a').get('href')
    

    return render(request, "new_search.html")


def new_search_1(request):
    search = request.POST.get('search')
    # models.Search.objects.create(search=search)
    final_url = ALIBABA_URL.format(search)
    response = requests.get(final_url)
    data = response.text 
    soup = BeautifulSoup(data, features='html.parser')
    # ------- ITEMS TO SCRAPE ------------
    items_list = soup.find_all(class_ = 'list-no-v2-inner m-gallery-product-item-v2 img-switcher-parent')
    item_name = soup.find(class_ = 'elements-title-normal__outter').get_text()
    item_price = soup.find(class_ = 'organic-gallery-offer-section__price').find('span').get_text()
    item_review = soup.find(class_ = 'seb-supplier-review text-ellipsis list-no-v2-decisionsup__element')
    item_url = soup.find(class_ = 'elements-title-normal one-line').get('href')
    item_image = soup.find(class_ = 'seb-img-switcher__imgs').get('data-image')

    


    final_item_list = []

    for items in items_list:
        item_name = items.find(class_ = 'elements-title-normal__outter').get_text()[0:30] + "..."
        item_price = items.find(class_ = 'organic-gallery-offer-section__price').find('span').get_text()    
        item_url = items.find(class_ = 'elements-title-normal one-line').get('href')
        item_image = items.find(class_ = 'seb-img-switcher__imgs').get('data-image')


        final_item_list.append((item_name, item_price, item_url, item_image))


    context = {
        'search': search,
        'final_item_list': final_item_list,
    }
    # return render(request, "new_search.html", context)