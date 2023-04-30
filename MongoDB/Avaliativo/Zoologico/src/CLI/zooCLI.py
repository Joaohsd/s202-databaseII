from Database.zooDAO import ZoologicoDAO

from Entity.animal import Animal
from Entity.caretaker import Cuidador
from Entity.habitat import Habitat

class ZoologicoCLI:
    def __init__(self, zooDao:ZoologicoDAO) -> None:
        self.__zooDao = zooDao

    def menu(self):
        # Flag
        menu = True
        while menu:
            # Mostra as opções do menu
            self.__showHeader()
            try:
                opcao = int(input('Entre com uma das opções apresentadas: '))
            except Exception as error:
                print(error + '\n')
                self.__showHeader()
                opcao = int(input('Entre com uma das opções apresentadas: '))
              
            # Verifica a opção digitada
            if opcao == 1:
                self.createAnimal()

            elif opcao == 2:
                animal = self.readAnimal()

                # Verifica se há um animal retornado
                if animal != None:
                    animal.printSelf()

            elif opcao == 3:
                self.updateAnimal()

            elif opcao == 4:
                self.deleteAnimal()
                
            else:
                self.__zooDao.disconnectDB()
                menu = False

    def __showHeader(self):
        print('Bem-vindo ao menu do Zoológico!')
        print('As opções são:')
        print('1 - Adicionar um animal ao Banco de dados')
        print('2 - Recuperar informações de um animal no Banco de dados')
        print('3 - Atualizar informações de um animal no Banco de dados')
        print('4 - Deletar um animal do Banco de dados')
        print('5 - Sair do Menu')

    def createAnimal(self):
        # Cuidador
        id = str(input('Entre com o ID do CUIDADOR: '))
        nome = str(input('Entre com o NOME do CUIDADOR: '))
        documento = str(input('Entre com o DOCUMENTO do CUIDADOR: '))
        cuidador = Cuidador(id=id, nome=nome, documento=documento)
        
        # Habitats
        habitatFlag = True
        habitats = []
        while habitatFlag:
            # Informações do Habitat
            id = str(input('Entre com o ID do HABITAT: '))
            nome = str(input('Entre com o NOME do HABITAT: '))
            ambiente = str(input('Entre com o TIPO DE AMBIENTE do HABITAT: '))
            # Cria o Habitat
            habitat = Habitat(id=id, nome=nome, tipoAmbiente=ambiente, cuidador=cuidador)
            habitats.append(habitat)
            opcaoHabitat = str(input('Deseja adicionar mais um HABITAT? S ou N: '))
            habitatFlag = True if opcaoHabitat == 'S' else False
        
        # Animal
        id = str(input('Entre com o ID do ANIMAL: '))
        nome = str(input('Entre com o NOME do ANIMAL: '))
        especie = str(input('Entre com a ESPECIE do ANIMAL: '))
        idade = int(input('Entre com a IDADE do ANIMAL: '))
        animal = Animal(id=id, nome=nome, especie=especie, idade=idade, habitats=habitats)

        # Inserindo o Animal no Banco de Dados
        self.__zooDao.createAnimal(animal=animal)

    def readAnimal(self) -> Animal:
        id = str(input('Entre com o ID do ANIMAL: '))
        animal = self.__zooDao.readAnimal(id=id)
        return animal

    def updateAnimal(self):
        id = str(input('Entre com o ID do ANIMAL: '))
        animal = self.__zooDao.readAnimal(id=id)
        
        if animal != None:
            print('INFORMAÇÕES DO ANIMAL A SER ATUALIZADO:')
            animal.printSelf()
            # Animal
            opt = str(input('Deseja alterar o NOME do Animal? S ou N: '))
            if opt == 'S':
                nome = str(input('Entre com o NOME do ANIMAL: '))
                animal.setNome(nome)
            opt = str(input('Deseja alterar a ESPECIE do Animal? S ou N: '))
            if opt == 'S':
                especie = str(input('Entre com a ESPECIE do ANIMAL: '))
                animal.setEspecie(especie)
            opt = str(input('Deseja alterar a IDADE do Animal? S ou N: '))
            if opt == 'S':
                idade = str(input('Entre com a IDADE do ANIMAL: '))
                animal.setIdade(idade)

            # Habitats
            for habitat in animal.getHabitats():
                habitat.printSelf()
                opt = str(input('Deseja alterar o NOME do HABITAT? S ou N: '))
                if opt == 'S':
                    nome = str(input('Entre com o NOME do HABITAT: '))
                    habitat.setNome(nome)
                opt = str(input('Deseja alterar o TIPO DE AMBIENTE do HABITAT? S ou N: '))
                if opt == 'S':
                    ambiente = str(input('Entre com o TIPO DE AMBIENTE do HABITAT: '))
                    habitat.setTipoAmbiente(ambiente)
                habitat.getCuidador().printSelf()
                opt = str(input('Deseja alterar as informações do CUIDADOR? S ou N: '))
                if opt == 'S':
                    opt = str(input('Deseja alterar o NOME do CUIDADOR? S ou N: '))
                    if opt == 'S':
                        nome = str(input('Entre com o NOME do CUIDADOR: '))
                        habitat.getCuidador().setNome(nome)
                    opt = str(input('Deseja alterar o DOCUMENTO do CUIDADOR? S ou N: '))
                    if opt == 'S':
                        documento = str(input('Entre com o DOCUMENTO do CUIDADOR: '))
                        habitat.getCuidador().setDocumento(documento)

            self.__zooDao.updateAnimal(animal=animal)


    def deleteAnimal(self):
        id = str(input('Entre com o ID do ANIMAL: '))
        self.__zooDao.deleteAnimal(id=id)
