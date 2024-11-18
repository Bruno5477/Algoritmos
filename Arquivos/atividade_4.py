def copiar_arquivo(origem,copia):

    try:
        with open(origem, "r", encoding= "UTF-8") as arquivo_origem:
            conteudo = arquivo_origem.read()

        with open(copia, "w", encoding= "UTF-8") as arquivo_copia:
            arquivo_copia.write(conteudo)

        print(f"Conteúdo copiado de '{origem}emra '{copia}' com sucesso.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{origem}emo foi encontrado.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

arquivo_origem = 'origem.txt'
arquivo_copia = 'copia.txt'

copiar_arquivo(arquivo_origem,arquivo_copia)