def dividir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, encoding="UTF-8") as arquivo:
            parte = 1
            linhas_atual = []
            
            for linha in arquivo:
                linhas_atual.append(linha)
                
                
                if len(linhas_atual) == 100:
                    nome_parte = f"parte{parte}.txt"
                    
                    with open(nome_parte, "w", encoding="UTF-8") as partes:
                        partes.writelines(linhas_atual)
                    print(f"{nome_parte} criado com sucesso.")
                    
                    parte += 1
                    linhas_atual = []
            
            
            if linhas_atual:
                nome_parte = f"parte{parte}.txt"
                
                with open(nome_parte, "w", encoding="UTF-8") as partes:
                    partes.writelines(linhas_atual)
                print(f"{nome_parte} criado com sucesso.")
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")


arquivo = "grande.txt"

dividir_arquivo(arquivo)
