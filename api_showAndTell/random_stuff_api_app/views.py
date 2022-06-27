from django.shortcuts import render, redirect, reverse
import requests
from dotenv import load_dotenv
import os
import json


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        tag = request.POST.get('category')
        url = "https://random-stuff-api.p.rapidapi.com/joke"
        querystring = {"tag": tag, "blacklist":"dirty, women"}
        load_dotenv()
        headers = {
            "Authorization": os.environ['apiKey'],
            "X-RapidAPI-Key": os.environ['rapidKey'],
            "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        my_data = {'response': json.loads(response.text)}
        return render(request, 'show_joke.html', my_data)
