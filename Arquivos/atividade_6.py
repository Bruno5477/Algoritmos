def substituir_palavra(nome_arquivo, antiga, nova):

    try:
        with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.read()

        conteudo_novo = conteudo.replace(antiga,nova)

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo_novo)

        print(f"Todas as ocorrências de '{antiga}' foram substituídas por '{nova}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

arquivo_nome = "atividade_6.txt"
palavra_antiga = "Python"
palavra_nova = "Programação"

substituir_palavra(arquivo_nome,palavra_antiga,palavra_nova)
