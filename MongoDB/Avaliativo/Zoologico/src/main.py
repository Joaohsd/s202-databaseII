from CLI.zooCLI import ZoologicoCLI
from Database.zooDAO import ZoologicoDAO

def main():
    # URL
    senha = str(input('Entre com a senha do Banco de Dados: '))
    url = 'mongodb+srv://zoologico:' + senha + '@cluster0.zwboxur.mongodb.net/test'

    zooDao = ZoologicoDAO(url=url, databaseName='Zoologico', collectionName='Animais')
    zooCli = ZoologicoCLI(zooDao=zooDao)
    
    # Inicializa o menu
    zooCli.menu()

if __name__ == '__main__':
    main()