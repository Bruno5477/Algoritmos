import random
import string

# função que gera uma senha aleatória
def gerar_senha(len):
    caracteres = string.ascii_letters + string.digits
    senha = "".join(random.choice(caracteres) for _ in range(len))
    return senha

def senha_criptografada(senha, desl, index=0):

    if index == len(senha):
        return ""
    
    caracter = senha[index]

    if caracter.isalpha():
        base = ord('A') if caracter.isupper() else ord('a')
        
        novo_char = chr((ord(caracter) - base + desl) % 26 + base)
    
    elif caracter.isdigit():
        novo_char = chr((ord(caracter) - ord('0') + desl) % 10 + ord('0'))
    
    else:
        novo_char = caracter

    return novo_char + senha_criptografada(senha, desl, index + 1)

senha = "A1b2C3d4"
senha_cripto = senha_criptografada(senha,3)

print(f"A senha original: {senha}")
print("Senha criptografada:", senha_cripto)