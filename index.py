import requests, json

url = ['https://pokeapi.co/api/v2/pokemon/cherrim',
       'https://pokeapi.co/api/v2/pokemon/fidough',
       'https://pokeapi.co/api/v2/pokemon/gastly',
        'https://pokeapi.co/api/v2/pokemon/heatran',
        'https://pokeapi.co/api/v2/pokemon/hydrapple',
       'https://pokeapi.co/api/v2/pokemon/pikachu',
        'https://pokeapi.co/api/v2/pokemon/butterfree',
        'https://pokeapi.co/api/v2/pokemon/machamp',
        'https://pokeapi.co/api/v2/pokemon/oddish',
        'https://pokeapi.co/api/v2/pokemon/kingler',
        'https://pokeapi.co/api/v2/pokemon/eevee',
        'https://pokeapi.co/api/v2/pokemon/snorlax',
        'https://pokeapi.co/api/v2/pokemon/jolteon',
        'https://pokeapi.co/api/v2/pokemon/flareon',
        'https://pokeapi.co/api/v2/pokemon/gengar',
        'https://pokeapi.co/api/v2/pokemon/magneton',
        'https://pokeapi.co/api/v2/pokemon/shellder',
        'https://pokeapi.co/api/v2/pokemon/diglett',
        'https://pokeapi.co/api/v2/pokemon/growlithe',
        'https://pokeapi.co/api/v2/pokemon/cloyster'
        ]

json_list = []

for links in url:
    data = requests.get(links)
    urls = data.json()
    json_list.append(urls)

def catch_em_all(pokelist):
    new_data = []
    for pokemon in pokelist:
        pokemon_dict = {}

        pokemon_dict = {
            'name' : pokemon['name'],
            'ability name' : pokemon['abilities'][0]['ability']['name'],
            'types': pokemon['types'][0]['type']['name'],
            'weight' : pokemon['weight']
        }

        new_data.append(pokemon_dict)
    return new_data

catch_em_all(json_list)