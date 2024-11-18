from collections import Counter
import string


def contar_palavras(nome_arquivo):

    try:
        with open(nome_arquivo, encoding="UTF-8") as arquivo:
            palavras = arquivo.read()

            palavras =palavras.translate(str.maketrans('', '', string.punctuation)).lower()

            palavras = palavras.split()
            
            contagem = Counter(palavras)

            for palavra, count in contagem.items():
                print(f"{palavra}:{count}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

arquivo = "texto.txt"
contar_palavras(arquivo)