from .database import Database

class PokedexDB(Database):
    def __init__(self, database, collection):
        super().__init__(database, collection)

    def printPokemons(self):
        pokemons = self.collection.find()
        for pokemon in pokemons:
            print(pokemon)

    def getPokemonByDex(self, number: int):
        return self.collection.find({"id": number})
    
    def getPokemonByType(self, type: str):
        return self.collection.find({"type":type})
    
    def getPokemonByNameInEnglish(self, name: str):
        return self.collection.find({"name.english":name})
    
    def getPokemonByTypeAndLifeGTEValue(self, type: str, hp: int):
        return self.collection.find({"type":type, "base.HP":{"$gte":hp}})
    
    def getPokemonByLifeLTValue(self, hp: int):
        return self.collection.find({"base.HP":{"$lt":hp}})