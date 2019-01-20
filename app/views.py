# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.db.models import Q

from  django.contrib import messages,auth
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
import random
#from selenium import webdriver
class cp:
    def __init__(self,course,review,rating,price,website):
        self.course=course
        self.review=review
        self.rating=round(random.uniform(2.3,5),1)
        self.price=price
        self.website=website

def home(request):
    return render(request,'home.html')
#def sortSecond(val):
#    return val[2]


def search(request):
    if request.method=='POST':
        search=request.POST['srh']


        if search:
             URL = "https://www.edureka.co/search/"+search
             URL2= "https://www.simpliv.com"+search
             r = requests.get(URL)
             soup = BeautifulSoup(r.text,'lxml')
             r2 = requests.get(URL)
             soup2 = BeautifulSoup(r2.text,'lxml')
             soup2.prettify()
             soup.prettify()
             event_containers =(soup.find_all('div',class_ = "textinfoleft"))
             reviews = soup.find_all('span',attrs = {'class':'totalreviews'})
             ratings  = soup.find_all('span',attrs = {'class':'rating'})
             prices = soup.find_all('div',class_ = "pricemain")
             names = soup.find_all('div',class_ = "course-desc")
             courses=[]
             review=[]
             rating=[]
             price=[]
             p=[]
             website=[]
             j=0
             for i in event_containers:
                 courses.append(i.h3.text)
                 website.append(URL)


             for i in reviews:
                 review.append(i.text)

             for i in ratings:
                 rating.append(i.text)
             for i in prices:
                 price.append(i.contents[0].text)


             for i in range(0,len(courses)):
                 p.append(cp(courses[i],review[i],rating[i],price[i],website[i]))


             return render(request,'home.html',{"all":sorted(p,key=lambda x: x.rating,reverse=True)})


        else:
            return HttpResponseRedirect('')
            return render(request,'home.html')

    return render(request,'home.html')
