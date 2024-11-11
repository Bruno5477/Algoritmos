"""Escreva uma função que verifica se uma senha
possui no mínimo 8 caracteres e pelo menos um número. Se a senha não
atender aos requisitos, levante uma exceção com uma mensagem
personalizada. Trate a exceção e mostre a mensagem ao usuário.
"""

def verificar_senha (senha):
    if len(senha) < 8 or not any(c in '0123456789' for c in senha):
        raise ValueError(f'A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.')
    
def testar_senha():
    try:
        senha = input(f"Digite uma senha: ")
        verificar_senha(senha)
        print(f'Senha válida!')
    
    except ValueError as e:
        print(f'Erro: {str(e)}')

testar_senha()
