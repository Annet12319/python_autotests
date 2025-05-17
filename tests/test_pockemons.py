import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ff79747377d8cae5231fa76736aa4698'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 33537

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200 

def test_part_of_response():
    responce = requests.get(url = f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
    data = responce.json()["data"]
    assert data[0]["trainer_name"] == "Anita"