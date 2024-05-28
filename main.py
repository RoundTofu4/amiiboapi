from fastapi import FastAPI
import json

app = FastAPI()

def load_amiibos_from_file():
    with open("amiibos.json") as f:
        amiibos = json.load(f)
    return amiibos

def extract_amiibo_names(amiibo_data):
    amiibo_names = [amiibo['name'] for amiibo in amiibo_data['amiibo']]
    return amiibo_names

def extract_amiibo_series(amiibo_data):
    amiibo_series = [amiibo['amiiboSeries'] for amiibo in amiibo_data['amiibo']]
    return amiibo_series

def extract_amiibo_character(amiibo_data):
    amiibo_character = [amiibo['character'] for amiibo in amiibo_data['amiibo']]
    return amiibo_character

def extract_amiibo_type(amiibo_data):
    amiibo_type = [amiibo['type'] for amiibo in amiibo_data['amiibo']]
    return amiibo_type

amiibos = load_amiibos_from_file()

@app.get("/amiibos")
def get_amiibos():
    return amiibos

@app.get("/series")
def get_series():
    amiibo_series = extract_amiibo_series(amiibos)
    return list(amiibo_series)

@app.get("/character")
def get_characters():
    amiibo_character = extract_amiibo_character(amiibos)
    return list(amiibo_character)

@app.get("/type")
def get_types():
    amiibo_type = extract_amiibo_type(amiibos)
    return list(amiibo_type)

@app.get("/name")
def get_names():
    amiibo_names = extract_amiibo_names(amiibos)
    return list(amiibo_names)

