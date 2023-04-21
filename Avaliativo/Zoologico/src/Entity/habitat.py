from Entity.caretaker import Cuidador

class Habitat:
    def __init__(self, id:str, nome:str, tipoAmbiente:str, cuidador:Cuidador):
        self.__id = id
        self.__nome = nome
        self.__tipoAmbiente = tipoAmbiente
        self.__cuidador = cuidador

    '''
        Getters
    '''
    def getId(self) -> str:
        return self.__id
    
    def getNome(self) -> str:
        return self.__nome
    
    def getTipoAmbiente(self) -> str:
        return self.__tipoAmbiente

    def getCuidador(self) -> Cuidador:
        return self.__cuidador
    
    '''
        Setters
    '''
    def setId(self, id):
        self.__id = id
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setTipoAmbiente(self, tipoAmbiente):
        self.__tipoAmbiente = tipoAmbiente

    def setCuidador(self, cuidador):
        self.__cuidador = cuidador

    '''
        Public Methods
    '''
    def printSelf(self):
        print('ID do HABITAT:', self.__id)
        print('NOME do HABITAT:', self.__nome)
        print('TIPO DE AMBIENTE do HABITAT:', self.__tipoAmbiente)