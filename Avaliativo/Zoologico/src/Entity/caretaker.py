class Cuidador:
    def __init__(self, id:str, nome:str, documento:str):
        self.__id = id
        self.__nome = nome
        self.__documento = documento

    '''
        Getters
    '''
    def getId(self) -> str:
        return self.__id
    
    def getNome(self) -> str:
        return self.__nome
    
    def getDocumento(self) -> str:
        return self.__documento
    
    '''
        Setters
    '''
    def setId(self, id):
        self.__id = id
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setDocumento(self, documento):
        self.__documento = documento

    '''
        Public Methods
    '''
    def printSelf(self):
        print('ID do CUIDADOR:', self.__id)
        print('NOME do CUIDADOR:', self.__nome)
        print('DOCUMENTO do CUIDADOR:', self.__documento)