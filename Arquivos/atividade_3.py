def contar_linhas_palavras(nome_arquivo):
    
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            total_linhas = len(linhas)
            total_palavras = sum(len(linha.split()) for linha in linhas)

            print(f"Total de linhas: {total_linhas}")
            print(f"Total de palavras: {total_palavras}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

nome_arquivo = "atividade_3.txt"
novo_arquivo = "grande.txt"
contar_linhas_palavras(nome_arquivo)
contar_linhas_palavras(novo_arquivo)