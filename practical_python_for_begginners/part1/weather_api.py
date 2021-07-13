import requests
from requests.api import get

def get_weather_desc_and_temp():
    api_key = "84a95ae1d1bf70c776087f5459d86230"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
def main():
    weather_dict = get_weather_desc_and_temp()
    print("Todays forecast is", weather_dict.get('description'))
    print("the minimum temperature is", weather_dict.get('temp_min'))
    print("the maximum temperature is", weather_dict.get('temp_max'))

main()
