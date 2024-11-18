import string

def criptografar(texto):
    
    resultado = []
    
    for char in texto:
        
        if char.isalpha():  # Apenas letras
            
            alfabeto = string.ascii_lowercase if char.islower() else string.ascii_uppercase
            # Substituir pelo próximo caractere no alfabeto
            novo_char = alfabeto[(alfabeto.index(char) + 1) % len(alfabeto)]
            resultado.append(novo_char)
        else:
            resultado.append(char)  
    
    return ''.join(resultado)

# Função para descriptografar o texto
def descriptografar(texto):
    resultado = []
    for char in texto:
        if char.isalpha():  # Apenas letras
            # Determinar o alfabeto (maiúsculas ou minúsculas)
            alfabeto = string.ascii_lowercase if char.islower() else string.ascii_uppercase
            # Substituir pelo caractere anterior no alfabeto
            novo_char = alfabeto[(alfabeto.index(char) - 1) % len(alfabeto)]
            resultado.append(novo_char)
        else:
            resultado.append(char)  # Mantém outros caracteres inalterados
    return ''.join(resultado)


arquivo_original = "secreto.txt"
arquivo_criptografado = "criptografado.txt"

# Criptografar o conteúdo do arquivo original
try:
    
    with open(arquivo_original) as entrada:
        conteudo = entrada.read()
        conteudo_criptografado = criptografar(conteudo)
    
    with open(arquivo_criptografado, "w") as saida:
        saida.write(conteudo_criptografado)
    
    print("Arquivo criptografado com sucesso! Conteúdo salvo em 'criptografado.txt'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_original}' não foi encontrado.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Descriptografar o conteúdo do arquivo criptografado
try:
    
    with open(arquivo_criptografado) as entrada:
        conteudo = entrada.read()
        conteudo_descriptografado = descriptografar(conteudo)
    
    print("\nConteúdo descriptografado:")
    print(conteudo_descriptografado)

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_criptografado}' não foi encontrado.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
