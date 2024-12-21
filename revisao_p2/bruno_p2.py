import os

# Função para cadastrar documentos históricos
def cadastrar_documento(arquivo):
    try:
        titulo = input("Título do documento: ").strip()
        data = input("Data de produção (aaaa-mm-dd): ").strip()
        tema = input("Tema: ").strip()
        contexto = input("Contexto histórico: ").strip()
        descricao = input("Descrição: ").strip()
        autor = input("Autor: ").strip()
        localizacao = input("Localização na biblioteca: ").strip()
        
        if not titulo or not data or not tema or not autor:
            raise ValueError("Campos obrigatórios estão faltando!")
        
        with open(arquivo, 'a', encoding='utf-8') as f:
            f.write(f"{titulo};{data};{tema};{contexto};{descricao};{autor};{localizacao}\n")
        
        print("Documento cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar documento: {e}")

# Função para listar documentos históricos ordenados por título
def listar_documentos(arquivo):
    try:
        if not os.path.exists(arquivo):
            raise FileNotFoundError("Arquivo de documentos não encontrado.")
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            documentos = f.readlines()
        
        documentos = [doc.strip().split(";") for doc in documentos]
        
        # Algoritmo de ordenação (Bubble Sort) por título
        for i in range(len(documentos)):
            for j in range(0, len(documentos) - i - 1):
                if documentos[j][0] > documentos[j + 1][0]:
                    documentos[j], documentos[j + 1] = documentos[j + 1], documentos[j]
        
        print("\nDocumentos cadastrados (ordenados por título):")
        for doc in documentos:
            print(f"Título: {doc[0]}, Autor: {doc[5]}, Data: {doc[1]}, Tema: {doc[2]}")
    except Exception as e:
        print(f"Erro ao listar documentos: {e}")

# Função para registrar empréstimos
def registrar_emprestimo(arquivo_emprestimos):
    try:
        documento = input("Título do documento emprestado: ").strip()
        evento = input("Nome do evento: ").strip()
        responsavel = input("Responsável pelo evento: ").strip()
        tema = input("Tema do evento: ").strip()
        periodo = input("Período de empréstimo (aaaa-mm-dd a aaaa-mm-dd): ").strip()
        
        if not documento or not evento or not periodo:
            raise ValueError("Campos obrigatórios estão faltando!")
        
        with open(arquivo_emprestimos, 'a', encoding='utf-8') as f:
            f.write(f"{documento};{evento};{responsavel};{tema};{periodo}\n")
        
        print("Empréstimo registrado com sucesso!")
    except Exception as e:
        print(f"Erro ao registrar empréstimo: {e}")

# Função para listar empréstimos
def listar_emprestimos(arquivo_emprestimos):
    try:
        if not os.path.exists(arquivo_emprestimos):
            raise FileNotFoundError("Arquivo de empréstimos não encontrado.")
        
        with open(arquivo_emprestimos, 'r', encoding='utf-8') as f:
            emprestimos = f.readlines()
        
        print("\nEmpréstimos registrados:")
        for emp in emprestimos:
            dados = emp.strip().split(";")
            print(f"Documento: {dados[0]}, Evento: {dados[1]}, Responsável: {dados[2]}, Tema: {dados[3]}, Período: {dados[4]}")
    except Exception as e:
        print(f"Erro ao listar empréstimos: {e}")

# Função principal para o menu
def menu():
    arquivo_documentos = "documentos.csv"
    arquivo_emprestimos = "emprestimos.csv"
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Documento")
        print("2. Listar Documentos")
        print("3. Registrar Empréstimo")
        print("4. Listar Empréstimos")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            cadastrar_documento(arquivo_documentos)
        elif escolha == "2":
            listar_documentos(arquivo_documentos)
        elif escolha == "3":
            registrar_emprestimo(arquivo_emprestimos)
        elif escolha == "4":
            listar_emprestimos(arquivo_emprestimos)
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
