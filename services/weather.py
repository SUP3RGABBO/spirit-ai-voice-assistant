"""
Weather service module for location-based weather retrieval.

This module provides:
- extraction of city names from natural language input
- fuzzy matching against a predefined global city database
- conversion of city names into API-compatible location strings
- retrieval of weather data from an external weather API

It handles fallback cases and returns natural language responses
ready to be used by the text-to-speech system.
"""

import requests
from difflib import get_close_matches
from config import weather_api_key, BASE_WEATHER_URL


CITIES_COUNTRIES = {
    # Italy
    "rome": "IT",
    "milan": "IT",
    "naples": "IT",
    "turin": "IT",
    "florence": "IT",
    "venice": "IT",
    "bologna": "IT",
    "genoa": "IT",
    "palermo": "IT",
    "catania": "IT",
    "bari": "IT",
    "verona": "IT",
    "messina": "IT",
    "padua": "IT",
    "trieste": "IT",
    "brescia": "IT",
    "taranto": "IT",
    "reggio calabria": "IT",
    "modena": "IT",
    "perugia": "IT",
    "prato": "IT",
    "parma": "IT",
    "bergamo": "IT",
    "busto arsizio": "IT",

    # USA
    "new york": "US",
    "los angeles": "US",
    "chicago": "US",
    "houston": "US",
    "phoenix": "US",
    "philadelphia": "US",
    "san antonio": "US",
    "san diego": "US",
    "dallas": "US",
    "san jose": "US",
    "austin": "US",
    "jacksonville": "US",
    "fort worth": "US",
    "columbus": "US",
    "charlotte": "US",
    "san francisco": "US",
    "indianapolis": "US",
    "seattle": "US",
    "denver": "US",
    "washington": "US",
    "boston": "US",
    "el paso": "US",

    # United Kingdom
    "london": "GB",
    "manchester": "GB",
    "birmingham": "GB",
    "leeds": "GB",
    "glasgow": "GB",
    "edinburgh": "GB",
    "liverpool": "GB",
    "bristol": "GB",
    "sheffield": "GB",
    "leicester": "GB",

    # France
    "paris": "FR",
    "marseille": "FR",
    "lyon": "FR",
    "toulouse": "FR",
    "nice": "FR",
    "nantes": "FR",
    "strasbourg": "FR",
    "montpellier": "FR",
    "bordeaux": "FR",
    "lille": "FR",

    # Germany
    "berlin": "DE",
    "munich": "DE",
    "hamburg": "DE",
    "cologne": "DE",
    "frankfurt": "DE",
    "stuttgart": "DE",
    "dusseldorf": "DE",
    "dortmund": "DE",
    "essen": "DE",
    "bremen": "DE",

    # Spain
    "madrid": "ES",
    "barcelona": "ES",
    "valencia": "ES",
    "seville": "ES",
    "zaragoza": "ES",
    "malaga": "ES",
    "murcia": "ES",
    "palma": "ES",
    "las palmas": "ES",
    "bilbao": "ES",

    # Japan
    "tokyo": "JP",
    "osaka": "JP",
    "nagoya": "JP",
    "sapporo": "JP",
    "fukuoka": "JP",
    "kobe": "JP",
    "kyoto": "JP",
    "yokohama": "JP",
    "kawasaki": "JP",
    "saitama": "JP",

    # China
    "beijing": "CN",
    "shanghai": "CN",
    "guangzhou": "CN",
    "shenzhen": "CN",
    "tianjin": "CN",
    "chongqing": "CN",
    "chengdu": "CN",
    "wuhan": "CN",
    "xian": "CN",
    "hangzhou": "CN",

    # Russia
    "moscow": "RU",
    "saint petersburg": "RU",
    "novosibirsk": "RU",
    "yekaterinburg": "RU",
    "nizhny novgorod": "RU",
    "kazan": "RU",
    "chelyabinsk": "RU",
    "omsk": "RU",
    "samara": "RU",
    "rostov": "RU",

    # Australia
    "sydney": "AU",
    "melbourne": "AU",
    "brisbane": "AU",
    "perth": "AU",
    "adelaide": "AU",
    "gold coast": "AU",
    "newcastle": "AU",
    "canberra": "AU",

    # Brazil
    "rio de janeiro": "BR",
    "sao paulo": "BR",
    "brasilia": "BR",
    "salvador": "BR",
    "fortaleza": "BR",
    "belo horizonte": "BR",
    "manaus": "BR",
    "curitiba": "BR",

    # Canada
    "toronto": "CA",
    "montreal": "CA",
    "vancouver": "CA",
    "calgary": "CA",
    "ottawa": "CA",
    "edmonton": "CA",
    "winnipeg": "CA",

    # India
    "delhi": "IN",
    "mumbai": "IN",
    "bangalore": "IN",
    "kolkata": "IN",
    "chennai": "IN",
    "hyderabad": "IN",
    "ahmedabad": "IN",

    # Mexico
    "mexico city": "MX",
    "guadalajara": "MX",
    "monterrey": "MX",

    # Indonesia
    "jakarta": "ID",
    "surabaya": "ID",
    "bandung": "ID",

    # South Korea
    "seoul": "KR",
    "busan": "KR",

    # Southeast Asia
    "singapore": "SG",
    "kuala lumpur": "MY",
    "bangkok": "TH",

    # Africa & Middle East
    "cairo": "EG",
    "alexandria": "EG",
    "nairobi": "KE",
    "lagos": "NG",

    # Nordic Countries
    "helsinki": "FI",
    "oslo": "NO",
    "stockholm": "SE",
    "copenhagen": "DK",
    "reykjavik": "IS",

    # Middle East
    "dubai": "AE",
    "doha": "QA",
    "riyadh": "SA",
    "tel aviv": "IL",

    # Eastern & Southern Europe
    "athens": "GR",
    "sofia": "BG",
    "bucharest": "RO",
    "warsaw": "PL",
    "prague": "CZ",
    "vienna": "AT",
    "zurich": "CH",
    "geneva": "CH",
    "lisbon": "PT",
    "porto": "PT",
    "dublin": "IE",
}


def extract_city(text):
    text_lower = text.lower()
    words = text_lower.split()
    city_list = list(CITIES_COUNTRIES.keys())


    for i in range(len(words)):

        match = get_close_matches(words[i], city_list, n=1, cutoff=0.7)
        if match:
            city_name = match[0]
            return f"{city_name},{CITIES_COUNTRIES[city_name]}"


        if i < len(words) - 1:
            combined = words[i] + " " + words[i + 1]
            match = get_close_matches(combined, city_list, n=1, cutoff=0.7)
            if match:
                city_name = match[0]
                return f"{city_name},{CITIES_COUNTRIES[city_name]}"


    return "rome,IT"


def get_weather(city_api):
    try:
        params = {
            "q": city_api,
            "appid": weather_api_key,
            "units": "metric",
            "lang": "en"
        }

        response = requests.get(BASE_WEATHER_URL, params=params, timeout=5)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            city_name = city_api.split(",")[0].capitalize()
            return f"In {city_name} it is {temp:.1f}°C with {desc}"
        else:
            return "I can't retrieve the weather right now."

    except requests.exceptions.ConnectionError:
        return "I can't connect to the Internet. Please check your network."
    except Exception:
        return "Unexpected error while retrieving the weather."
