from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def index(request):
    city = request.POST.get('city', 'indore')

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=db2e02e0a46b72115018b6756eca7a9a'
    PARAMS = {'units':'metric'}

    # Google Custom Search API setup
    API_KEY = 'AIzaSyBGcD-eyz_Lcy0MpATD3Vny6Q1fFIXllxA'
    SEARCH_ENGINE_ID = '53783c46f8ea64351'
    query = f"{city} 1920x1080"
    start = 1
    searchType = 'image'
    city_url = f'https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={API_KEY}&searchType={searchType}&start={start}'

    try:
        # Weather API request
        weather_data = requests.get(weather_url, params=PARAMS).json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']

        # Google image search
        city_data = requests.get(city_url).json()
        search_items = city_data.get("items", [])
        if len(search_items) > 0:
            image_url = search_items[0]['link']
        else:
            image_url = ''  # fallback if no image

        exception_occurred = False

    except Exception as e:
        messages.error(request, f"Error fetching data: {e}")
        description = 'clear sky'
        icon = '01d'
        temp = 25
        city = 'indore'
        image_url = ''
        exception_occurred = True

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
        'exception_occurred': exception_occurred,
        'image_url': image_url
    })
