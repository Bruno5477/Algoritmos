def combinar_arquivos(origem, destino):

    try:
        with open(destino, "w", encoding="UTF-8") as arquivos:
            for arquivo in origem:
                
                try:
                    with open(arquivo, "r", encoding="UTF-8") as originais:
                        conteudo = originais.read()
                        arquivos.write(conteudo + "\n")

                except FileNotFoundError:
                    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
                
                except Exception as e:
                    print(f"Um erro ocorreu com o arquivo '{arquivo}': {e}")

        print(f"Arquivos combinado com sucesso no arquivo '{destino}'.")

    except Exception as e:
        print(f"Um erro ocorreu ao criar o arquivo de destino '{destino}': {e}")

arquivos_origem = ['parte1.txt', 'parte2.txt', 'parte3.txt']
arquivo_destino = 'texto_completo.txt'
combinar_arquivos(arquivos_origem, arquivo_destino)