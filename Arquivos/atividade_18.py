import csv

def validar_linha(nome, idade, email):
    
    try:        
        idade_valida = int(idade) > 0
        
        email_valido = '@' in email
        
        return idade_valida and email_valido
    
    except ValueError:        
        return False

def validar_dados_csv(arquivo_entrada, arquivo_saida):
    
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as entrada, \
             open(arquivo_saida, 'w', encoding='utf-8', newline='') as saida_erros:
            
            leitor = csv.reader(entrada)
            escritor = csv.writer(saida_erros)            
            
            for linha in leitor:
                if len(linha) != 3:  
                    escritor.writerow(linha) 
                    continue
                
                nome, idade, email = linha
                if not validar_linha(nome, idade, email):
                    escritor.writerow(linha)  
            
            print(f"Validação concluída. Linhas inválidas salvas em '{arquivo_saida}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


arquivo_origem = "dados.csv"
arquivo_erros = "erros.csv"
validar_dados_csv(arquivo_origem, arquivo_erros)
