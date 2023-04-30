from classes import *

def main():
    # Entrada de dados
    nome = str(input('Entre com o nome do elefante: '))
    idade = int(input('Entre com a idade do elefante: '))
    especie = str(input('Entre com a espécie do elefante: '))
    cor = str(input('Entre com a cor do elefante: '))
    tamanho = str(input('Entre com o tamanho do elefante: '))

    # Instância do elefante
    elefante = Elefante(nome, idade, especie, cor, tamanho)

    # Exibindo as informações solicitadas
    elefante.trombar()
    print(elefante.get_tamanho())

    if elefante.get_especie() == 'Africano' and elefante.get_idade() < 10:
        elefante.mudar_tamanho('pequeno')
        elefante.mudar_som('Paaah')
    elif elefante.get_especie() == 'Africano':
        elefante.mudar_tamanho('grande')
        elefante.mudar_som('PAHHHHHH')

    # Exibindo as informações solicitadas
    elefante.trombar()
    print(elefante.get_tamanho())

if __name__ == '__main__':
    main()