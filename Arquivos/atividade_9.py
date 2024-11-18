def extrair(nome_arquivo):

    try:
        with open(nome_arquivo, encoding="UTF-8") as arquivo:
            print("Os nomes encontrados no arquivo foram: ")

            for linha in arquivo:
                partes = linha.split(",")

                for parte in partes:
                    if "Nome:" in parte:
                        nome = parte.split("Nome:")[1].strip()
                        print(f"- {nome}.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

arquivo = "pessoas.txt"
extrair(arquivo)