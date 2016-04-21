#!/usr/bin/env python2
#encoding: windows-1250

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import json
import requests
from StringIO import StringIO
import urllib

from PIL import Image

print "CheapShark API games search engine by Trykon"


print "What do you want to look for?"
print "Games or Deals ?"
a = raw_input("")
a = a.lower()

while((a != "games") & (a != "deals")):
    print "Enter correct value: \"Games\" or \"Deals\""
    a = raw_input("").lower()

if(a == "games"):
    print "Great!"
    print "Now what game are you looking for?"
    print "Give me a title..."
    b = str(raw_input(""))
    url = 'http://www.cheapshark.com/api/1.0/games?title=' + b
    resp = requests.get(url)
    jresponse = resp.json()
    for item in jresponse:
        print item['external']
    if (len(jresponse) < 1):
        print "what a shame, there is nothing like this ", b
    
elif(a=="deals"):
    print "Awesome!"
    print "Now tell me. Do you want to look by title? Y/N"
    title = ""
    lowPrice = ""
    upPrice = ""
    sale = ""
    sort=""
    if (raw_input().lower() == "y"):
        print "Give me a title then..."
        title = "title=" + raw_input()
    print "Do you want to set the lowest price? Y/N"
    if (raw_input().lower() == "y"):
        print "Give me a price then..."
        lowPrice = "lowerPrice=" + raw_input()
    print "Do you want to set the highest price? Y/N"
    if (raw_input().lower() == "y"):
        print "Give me a price then..."
        upPrice = "upperPrice=" + raw_input()
    print "Do you want to search only for sale deals? Y/N"
    if (raw_input().lower() == "y"):
        sale = "onSale=1"
    print "Do you want to sort the list? Y/N"
    if (raw_input().lower() == "y"):
        print "Tell me then by which parameter we will sort..."
        print "Title"
        print "Price"
        print "Release"
        sort = raw_input()
        if(sort.lower() == "title"):
            sort = "sortBy=" + sort
        elif(sort.lower() == "price"):
            sort = "sortBy=" + sort
        elif(sort.lower() == "release"):
            sort = "sortBy=" + sort
        else:
            sort = ""
    url = 'http://www.cheapshark.com/api/1.0/deals?'
    if(title != ""):
        url = url + "&" + title
    if(lowPrice != ""):
        url = url + "&" + lowPrice
    if(upPrice != ""):
        url = url + "&" + upPrice
    if(sale != ""):
        url = url + "&" + sale
    if(sort != ""):
        url = url + "&" + sort
    resp = requests.get(url)
    jresponse = resp.json()
    for item in jresponse:
        print item['title']
        print "     Sale price:", item['salePrice']
        print "     Normal price", item['normalPrice']
        #URL2 = item['thumb']
        #img = Image.open(StringIO(requests.get(URL2).content))
        #img.show()
    if(len(jresponse) < 1):
        print "Sorry but there is nothing that your match criteria..."
print "Thanks for using!"