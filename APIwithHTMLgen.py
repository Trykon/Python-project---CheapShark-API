#!/usr/bin/env python2
#encoding: windows-1250

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import json
import requests
import urllib
import webbrowser
import os
import time
import urllib

f = open('APIout.html','w')
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
    message = """
    <html>
    <head>
        <link rel="stylesheet" href="Bootstrap/bootstrap-3.3.5-dist/css/bootstrap.css" type="text/css"/>
    </head>
    <body>
        <h3>You have found:</h3>
    """
    for item in jresponse:
        message = message + ("""
        <div class="row">
        <div class="col-md-1">
        </div>
        <div class="col-md-5">
        <img align="right" src=\"""" + urllib.quote(item['thumb']).replace("%3A",":").replace("%5C","\\").replace("%3F","?").replace("%3D","=") + """\" alt="Image not found">
        </div>
        <div class="col-md-4">
        <p>Title: """ + item['external'] + """</p>
        <p>Cheapest price: <a href=\"""" + "http://www.cheapshark.com/redirect?dealID=" + item['cheapestDealID'] + """\">""" + item['cheapest'] + """</a></p>
        </div>
        <div class="col-md-2">
        </div>
        </div>
        """)
    if (len(jresponse) < 1):
        message = """
        <p>what a shame, there is nothing like what you were looking for</p>
        """
    message = message + """
    </body>
    </html>
    """
elif(a=="deals"):
    print "Awesome!"
    print "Now tell me. Do you want to look by title? Y/N"
    title = ""
    lowPrice = ""
    upPrice = ""
    sale = ""
    sort=""
    tit=raw_input()
    tit = tit.lower()
    if (tit == "y"):
        print "Give me a title then..."
        title = "title=" + raw_input()
    elif(tit != "n"):
        title = "title=" + tit
    print "Do you want to set the lowest price? Y/N"
    check = raw_input().lower()
    if (check == "y"):
        print "Give me a price then..."
        lowPrice = "lowerPrice=" + raw_input()
    elif(check != "n"):
        lowPrice = "lowerPrice=" + check
    print "Do you want to set the highest price? Y/N"
    check = raw_input().lower()
    if (check == "y"):
        print "Give me a price then..."
        upPrice = "upperPrice=" + raw_input()
        if lowPrice == "":
            lowPrice = "lowerPrice=0"
    elif(check != "n"):
        upPrice = "upperPrice=" + check
        if lowPrice == "":
            lowPrice = "lowerPrice=0"
    print "Do you want to search only for sale deals? Y/N"
    check = raw_input().lower()
    if (check == "y"):
        sale = "onSale=1"
    print "Do you want to sort the list? Y/N"
    if (raw_input().lower() == "y"):
        print "Tell me then by which parameter we will sort..."
        print "Title"
        print "Price"
        print "Release"
        sort = raw_input()
        sort = sort.lower()
        if(sort == "title"):
            sort = "sortBy=" + sort
        elif(sort == "price"):
            sort = "sortBy=" + sort
        elif(sort == "release"):
            sort = "sortBy=" + sort
        else:
            sort = ""
    url = 'http://www.cheapshark.com/api/1.0/deals?'
    ch=0
    if(title != ""):
        url = url + title
        ch=1
    if((lowPrice != "") & (ch==1)):
        url = url + "&" + lowPrice
    elif(lowPrice != ""):
        url = url + lowPrice
        ch=1
    if((upPrice != "") & (ch==1)):
        url = url + "&" + upPrice
    elif(upPrice != ""):
        url= url + upPrice
        ch=1
    if((sale != "") & (ch==1)):
        url = url + "&" + sale
    elif(sale!= ""):
        url = url + sale
        ch=1
    if((sort != "") & (ch==1)):
        url = url + "&" + sort
    elif(sort != ""):
        url = url + sort
    resp = requests.get(url)
    jresponse = resp.json()
    message = """
    <html>
    <head>
        <link rel="stylesheet" href="Bootstrap/bootstrap-3.3.5-dist/css/bootstrap.css" type="text/css"/>
    </head>
    <body>
        <h3>You have found:</h3>
    """
    for item in jresponse:
        message = message + """
        <div class="row">
        <div class="col-md-1">
        </div>
        <div class="col-md-5">
        <img align="right" src=\"""" + urllib.quote(item['thumb']).replace("%3A",":").replace("%5C","\\").replace("%3F","?").replace("%3D","=") + """\" alt="Image not found">
        </div>
        <div class="col-md-4">
        <p>Title: """ + item['title'] + """</p>
        <p>"""
        
        if(item['isOnSale']=="1"):
            message = message + """This game is on sale</p>
            <p>Sale price: """ + item['salePrice'] + """</p>"""
            
        else:
            message = message + "This game is not on sale</p>"
        message = message + """
        <p>Standard price: """ + item['normalPrice'] + """</p>
        <p>Rating: """ + str(item['steamRatingText']) + """</p>
        <p>You can get it <a href=\"""" + "http://www.cheapshark.com/redirect?dealID=" + item['dealID'] + """\">here</a></p>
        </div>
        <div class="col-md-2">
        </div>
        </div>
        """
    if(len(jresponse) < 1):
        message = message + "<p>Sorry but there is nothing that your match criteria...</p>"
    message = message + """
    </body>
    </html>
    """

f.write(message)
f.close()
webbrowser.open_new_tab('APIout.html')
time.sleep(2)
os.remove('APIout.html')