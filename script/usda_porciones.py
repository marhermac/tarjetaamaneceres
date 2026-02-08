import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("USDA_API_KEY")
BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def obtener_porcion_usda(nombre):
    params = {
        "query": nombre,
        "pageSize": 1,
        "api_key": API_KEY
    }

    r = requests.get(BASE_URL, params=params)
    if r.status_code != 200:
        return None, None

    data = r.json()
    foods = data.get("foods", [])
    if not foods:
        return None, None

    food = foods[0]

    for portion in food.get("foodPortions", []):
        if portion.get("gramWeight"):
            return portion.get("gramWeight"), "USDA"

    return None, None
