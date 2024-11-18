# Função para remover linhas vazias de um arquivo
def remover_linhas_vazias(arquivo_entrada, arquivo_saida):
    
    try: 
        with open(arquivo_entrada) as entrada:
            linhas = entrada.readlines()
        
        linhas_sem_vazios = [linha for linha in linhas if linha.strip()]        
        
        with open(arquivo_saida, "w") as saida:
            saida.writelines(linhas_sem_vazios)
        
        print(f"Linhas vazias removidas e conteúdo salvo em '{arquivo_saida}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


arquivo_origem = "com_vazios.txt"
arquivo_destino = "sem_vazios.txt"


remover_linhas_vazias(arquivo_origem, arquivo_destino)
