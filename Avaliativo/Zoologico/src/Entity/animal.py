from Entity.habitat import Habitat
from Entity.caretaker import Cuidador

from typing import List

class Animal:
    def __init__(self) -> None:
        pass

    def __init__(self, id:str = None, nome:str = None, especie:str = None, idade:int = None, habitats:List[Habitat] = []):
        self.__id = id
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade
        self.__habitats = habitats

    '''
        Getters
    '''
    def getId(self) -> str:
        return self.__id
    
    def getNome(self) -> str:
        return self.__nome
    
    def getEspecie(self) -> str:
        return self.__especie
    
    def getIdade(self) -> int:
        return self.__idade
    
    def getHabitats(self) -> List[Habitat]:
        return self.__habitats
    
    '''
        Setters
    '''
    def setId(self, id):
        self.__id = id
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setEspecie(self, especie):
        self.__especie = especie
    
    def setIdade(self, idade):
        self.__idade = idade
    
    def setHabitats(self, habitats):
        self.__habitats = habitats

    '''
        Public Methods
    '''
    def printSelf(self):
        # Animal
        print()
        print('ID do ANIMAL:', self.__id)
        print('NOME do ANIMAL:', self.__nome)
        print('ESPECIE do ANIMAL:', self.__especie)
        print('IDADE do ANIMAL:', self.__idade)
        print()
        # Habitats
        for habitat in self.__habitats:
            # Habitat
            habitat.printSelf()
            print()
            cuidador = habitat.getCuidador()
            # Cuidador
            cuidador.printSelf()
            print()
            