class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        # Atributos protegidos para serem acessados pela classe ou pelas classes filhas
        self._nome = nome
        self._idade = idade
        self._especie = especie
        self._cor = cor
        self._som = som

    def emitir_som(self):
        print('Som do Animal: ' + self._som)

    def mudar_cor(self, nova_cor):
        self._cor = nova_cor

    # Criei para poder modificar o atributo protegido
    def mudar_som(self, som):
        self._som = som
    
    def get_especie(self):
        return self._especie

    def get_idade(self):
        return self._idade

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, tamanho, som='VEEEE'):
        super().__init__(nome, idade, especie, cor, som)
        self.__tamanho = tamanho

    # Já tem o método que emite o som do animal... Coloquei assim para diferenciar!
    # Não faria sentido ter um método que apenas chama o outro método
    def trombar(self):
        print('Som do Elefante: ' + self._som)

    def mudar_tamanho(self, novo_tamanho):
        self.__tamanho = novo_tamanho

    # Criei para poder acessar o atributo privado
    def get_tamanho(self):
        return self.__tamanho
