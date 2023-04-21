from Database.database import Database

from Entity.animal import Animal
from Services.animalService import AnimalService

class ZoologicoDAO:
    def __init__(self, url:str, databaseName, collectionName):
        self.__db = Database(url, databaseName, collectionName)

    def createAnimal(self, animal:Animal) -> str:
        # Converte o objeto Animal para um documento Json
        documentoAnimal = AnimalService.setJsonDocumentByAnimal(animal=animal)
        
        try:
            result = self.__db.collection.insert_one(documentoAnimal)
            animal_id = result.inserted_id
            print(f"Animal {animal.getNome()} created with id: {animal_id}")
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")

    def readAnimal(self, id: str) -> Animal:
        try:
            result = self.__db.collection.find_one({"_id": id})
            if result:
                print(f"Animal found: {result}")

                # Converte o documento Json para um objeto Animal
                animal = AnimalService.setAnimalByJson(document=result)

                return animal
            else:
                print(f"No animal found with id {id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")

    def updateAnimal(self, animal:Animal):
        # Converte o objeto Animal para um documento Json
        documentoAnimal = AnimalService.setJsonDocumentByAnimal(animal=animal)
        try:
            result = self.__db.collection.update_one({"_id": animal.getId()}, {"$set": documentoAnimal})
            if result.modified_count:
                print(f"Animal {animal.getId()} updated.")
            else:
                print(f"No animal found with id {animal.getId()}")
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")

    def deleteAnimal(self, id: str):
        try:
            result = self.__db.collection.delete_one({"_id": id})
            if result.deleted_count:
                print(f"Animal {id} deleted")
            else:
                print(f"No animal found with id {id}")
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")

    def disconnectDB(self):
        self.__db.disconnect()