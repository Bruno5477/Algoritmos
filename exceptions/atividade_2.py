"""Capturando exceções múltiplas: Crie um programa que peça ao usuário o
nome de uma cor e mostre seu valor em RGB de acordo com um dicionário
pré-definido. O programa deve tratar exceções caso o nome da cor não exista
no dicionário.
cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul':
(0, 0, 255)}"""

def cores_rgb ():

    cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

    try:
        cor = input("Insira o nome da cor desejada: ").lower()
        rgb = cores[cor]

        print(f"O valor RGB para a cor {cor} é: {rgb}")
    
    except KeyError:

        print(f"Erro: A cor {cor} especificada não está no dicionário.")

cores_rgb()