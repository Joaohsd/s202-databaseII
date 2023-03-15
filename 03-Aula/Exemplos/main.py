from database import Database

import json
import os
from bson import json_util

def print_pokemons(pokemons):
    for pokemon in pokemons:
        print(pokemon)

def writeToJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})


db = Database(database='dex', collection='pokemons')
db.resetDatabase()
pks = db.collection.find()

if pks != None:
    print_pokemons(pokemons=pks)
else:
    print('não há pokemons')

bulbasaur = getPokemonByDex(1)
writeToJson(bulbasaur, "bulbasaur")