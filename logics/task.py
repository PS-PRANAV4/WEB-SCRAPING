from __future__ import absolute_import, unicode_literals
from celery import shared_task
from requests_html import HTMLSession
from .models import Plan

@shared_task
def add(x,y):
    try:    
        url = 'https://www.airtel.in/myplan-infinity/'

        s = HTMLSession()
        r = s.get(url)
        r.html.render(timeout=500)

        p = r.html.find('.border-bottom')
        g = r.html.find('.price')
        l = len(p)
        count = 0
        number = 4
        k = 0
        for i in range(0,l,4):
            details = p[i].text + p[i+1].text + p[i+2].text + p[i+3].text
            user = Plan.objects.create(price = g[k].text, details  = details)
            k = k+1
    except Exception as e:
        return e    
            
            
    return True