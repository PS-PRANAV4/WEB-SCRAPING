from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView,Response
from selenium import webdriver
from logics.task import add
from .models import Plan,PlanSerializer


class GetScrapedData(APIView):
    url = 'https://www.airtel.in/myplan-infinity/'
    def get(self,request):
        try:
            add.delay(4,5)
        except:
            pass
        return Response({"status":"success"},status=200) 
   
class GetData(APIView):

    def get(self,request):
        try:
            data = Plan.objects.all()[:4]
        except:
            Response({},status=400)
        
        plan = PlanSerializer(data, many = True)
        return Response(plan.data,status=200)