from db.pokedexDB import PokedexDB
import json
import os
from bson import json_util

def writeToJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                    indent=4,
                    separators=(',', ': '))

def main():
    # Opening the dataset
    with open('./dataset/pokedex.json',encoding='utf8') as pk:
        dataset = json.load(pk)

    # Instance of object to access DB
    pks = PokedexDB(database='dex', collection='pokemons')
    pks.resetDatabase(dataset)

    # Get pokemon with index equal to 2
    pk1 = pks.getPokemonByDex(number=25)
    writeToJson(pk1, 'pokemonByDex')

    # Get pokemons with type equal to Fire
    pk2 = pks.getPokemonByType(type='Fire')
    writeToJson(pk2, 'pokemonByType')

    # Get pokemon with name in english equal to Charizard
    pk3 = pks.getPokemonByNameInEnglish(name='Charizard')
    writeToJson(pk3, 'pokemonByNameEnglish')

    # Get pokemons with type equal to Water and life greater than or equal to 50
    pk4 = pks.getPokemonByTypeAndLifeGTEValue(type='Water', hp=50)
    writeToJson(pk4, 'pokemonByTypeAndLife')

    # Get pokemons with life less than 30
    pk5 = pks.getPokemonByLifeLTValue(hp=30)
    writeToJson(pk5, 'pokemonByLife')

    exit(1)

if __name__ == "__main__":
    main()