from fastapi import FastAPI
import json

app = FastAPI()

def load_amiibos_from_file():
    with open("amiibos.json") as f:
        amiibos = json.load(f)
    return amiibos

amiibos = load_amiibos_from_file()

@app.get("/amiibos")
def get_amiibos():
    return amiibos

@app.get("/series")
def get_series():
    series = set(amiibo["amiiboSeries"] for amiibo in amiibos)
    print (list(series))
    return list(series)

@app.get("/character")
def get_characters():
    characters = set(amiibo["character"] for amiibo in amiibos)
    return list(characters)

@app.get("/type")
def get_types():
    types = set(amiibo["type"] for amiibo in amiibos)
    return list(types)

@app.get("/name")
def get_names():
    names = list(map(lambda x: x["name"], amiibos))
    return names
