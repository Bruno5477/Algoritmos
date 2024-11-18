import shutil
from datetime import datetime

def backup_arquivo(origem, destino):
    try:
        # Copiar o conteúdo do arquivo de origem para o destino
        shutil.copyfile(origem, destino)
        
        with open(destino, "a", encoding="UTF-8") as backup:
            hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            backup.write(f'\nBackup realizado em: {hora}\n')
        
        print(f"Backup concluído com sucesso em {hora}!")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{origem}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

arquivo_origem = "dados.txt"
arquivo_backup = "backup.txt"

backup_arquivo(arquivo_origem,arquivo_backup)