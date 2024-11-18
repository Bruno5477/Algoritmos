
def copiar_arquivo_binario(origem, destino):
    
    try:        
        with open(origem, "rb") as arquivo_origem:            
            conteudo = arquivo_origem.read()
        
        with open(destino, "wb") as arquivo_destino:            
            arquivo_destino.write(conteudo)
        
        print(f"Arquivo copiado com sucesso para '{destino}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{origem}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


arquivo_origem = "imagem.jpg"
arquivo_destino = "imagem_copia.jpg"
copiar_arquivo_binario(arquivo_origem, arquivo_destino)
