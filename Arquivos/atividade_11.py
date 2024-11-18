def ordenar_nomes(nome_arquivo, saida):
    
    try:
        with open(nome_arquivo,  encoding="UTF-8") as arquivo:
            nomes = arquivo.readlines()  

        
        nomes = [nome.strip() for nome in nomes]  
        nomes.sort()  

        with open(saida, "w", encoding="UTF-8") as arquivo:
            for nome in nomes:
                arquivo.write(nome + '\n')  

        print(f"Nomes ordenados gravados em '{saida}' com sucesso.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

arquivo_nomes = "nomes.txt"
arquivo_saida = "nomes_ordenados.txt"

ordenar_nomes(arquivo_nomes,arquivo_saida)