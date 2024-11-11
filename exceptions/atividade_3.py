"""Bloco else e finally: Escreva um programa que solicite um número ao
usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o
número é válido. Utilize o bloco else para imprimir que o programa foi
executado com sucesso, e o bloco finally para imprimir "Programa
encerrado".
"""
def verficar_num ():

    try:
        num = int(input("Digite um número: "))

        if num > 10:
            print(f"O número {num} é válido.")

       
    except ValueError:
        print(f"Erro: O {num} não é válido, insira um número inteiro maior do que 10.")
    
    else:
        print(f"O programa foi executado com sucesso.")
    
    finally:
        print(f"Programa encerrado.")

verficar_num()