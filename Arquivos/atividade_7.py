import os

def listar(caminho_diretorio):

    try:
        itens = os.listdir(caminho_diretorio)

        if not itens:
            print(f"O diretório '{caminho_diretorio}' está vázio.")
        
        else:
            print(f"Conteúdo do diretório '{caminho_diretorio}': ")

            for item in itens:
                tipo = "Diretório" if os.path.isdir(os.path.join(caminho_diretorio,item)) else "Arquivo"
                print(f" - {item} ({tipo})")

    except FileNotFoundError:
        print(f"Erro: O diretório '{caminho_diretorio}' não foi encontrado.")
    
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o diretório '{caminho_diretorio}'.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

caminho = input("Informe o caminho do diretório: ")

listar(caminho)