
import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '81ee2c14f8a9addf2a0ae83e9e852796'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '30717'

def test_status_code_trainer200():
    trainers = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert trainers.status_code == 200

def test_name_trainerJVenko():
    trainers = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert trainers.json()['trainer_name'] == 'JVenko'