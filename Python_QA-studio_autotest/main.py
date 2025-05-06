import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '81ee2c14f8a9addf2a0ae83e9e852796'
HEADER = {
    'Content-type': 'application/json',
    'trainer_token': TOKEN
}

# Создание покемона
body_create_pokemon = {
    "name": "Yoshenka",
    "photo_id": 962
}

create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(create.text)

# Получение ID покемона из ответа
create_response = create.json()
pokemon_number = create_response.get('id')


# Изменение имени покемона
body_change_name = {
    "pokemon_id": pokemon_number,
    "name": "New Name",
    "photo_id": 572
}

change_name = requests.put(url=f'{URL}/pokemons/{pokemon_number}', headers=HEADER, json=body_change_name)
print(change_name.text)

# Поймать покемона в покеболл
body_catch_pokemon = {
    "pokemon_id": pokemon_number
}

catch_in_poketball = requests.post(
    url=f'{URL}/trainers/add_pokeball',
    headers=HEADER,
    json=body_catch_pokemon
)
print(catch_in_poketball.text)
