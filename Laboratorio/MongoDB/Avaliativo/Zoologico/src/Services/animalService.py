from Entity.animal import Animal
from Entity.habitat import Habitat
from Entity.caretaker import Cuidador

from typing import Dict

class AnimalService:
    @staticmethod
    def setAnimalByJson(document) -> Animal:
        # Informações do Animal
        id = document["_id"]
        nome = document["nome"]
        especie = document["especie"]
        idade = document["idade"]

        # Habitats
        habitats = []

        # Varrendo o array no documento
        for auxHabitat in document["habitats"]:
            cuidador = Cuidador(id=auxHabitat["cuidador"]["_id"], nome=auxHabitat["cuidador"]["nome"], documento=auxHabitat["cuidador"]["documento"])
            habitat = Habitat(id=auxHabitat["_id"], nome=auxHabitat["nome"], tipoAmbiente=auxHabitat["tipoAmbiente"],cuidador=cuidador)
            habitats.append(habitat)
        
        # Cria um Animal
        animal = Animal(id=id, nome=nome, especie=especie, idade=idade, habitats=habitats)

        return animal
    
    @staticmethod
    def setJsonDocumentByAnimal(animal:Animal) -> Dict:
        # Cria um documento baseado no Animal
        documentoAnimal = {
            "_id": animal.getId(),
            "nome": animal.getNome(),
            "especie": animal.getEspecie(),
            "idade": animal.getIdade(),
            "habitats": []
        }
        # Adiciona os Habitats ao documento
        for habitat in animal.getHabitats():
            documentoAnimal["habitats"].append(
                {
                    "_id": habitat.getId(), 
                    "nome": habitat.getNome(), 
                    "tipoAmbiente": habitat.getTipoAmbiente(),
                    "cuidador":{
                        "_id": habitat.getCuidador().getId(),
                        "nome": habitat.getCuidador().getNome(),
                        "documento": habitat.getCuidador().getDocumento()
                    }
                }
            )
        
        return documentoAnimal