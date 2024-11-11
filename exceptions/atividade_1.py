"""Tratamento de exceções básicas: Escreva um programa que peça ao usuário
dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir
um valor inválido ou tentar dividir por zero, o programa deve exibir uma
mensagem de erro apropriada"""

def divisao ():
    try:
        
        num_1 = float(input("Digite o primeiro número, que será o dividendo: "))
        num_2 = float(input("Digite o segundo número, que será o divisor: "))
        resultado = num_1/num_2
        print(f"O resultado da divisão é: {resultado:.2f}")

    except ValueError as e:
        
        print(f"Erro: {e} está incorreto, insira apenas números válidos.")
    
    except ZeroDivisionError:
        print(f"Erro: Não é possível dividir por zero.")

divisao()