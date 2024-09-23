estoque_livros = []

# Cadastrar um livro
def cadastrar_livro(titulo:str, autor: str, genero: str, quantidade: int, codigo: str):

    livro = {
        "Título": titulo,
        "Autor": autor,
        "Gênero": genero,
        "Quantidade": quantidade,
        "Código": codigo
    }

    estoque_livros.append(livro)

    print(f"O Livro {titulo} foi cadastrado no sistema com sucesso!")

# Buscar livro
def buscar_livro(codigo: str):
    for livro in estoque_livros:
        if livro["Código"] == codigo:
            return livro
            
    return None

# Atualizar Estoque de um Livro
def atualizar_estoque(codigo, nova_quantidade):
    livro = buscar_livro(codigo)
    if livro:
        livro["Quantidade"] = nova_quantidade
        print(f"Estoque do livro '{livro['Título']}' foi atualizado para {nova_quantidade} unidades.")
    
    else:
        print("Erro: Livro não encontrado.")

# Remover livro
def remover_livro(codigo):
    livro = buscar_livro(codigo)
    if livro:
        estoque_livros.remove(livro)
        print(f"O Livro '{livro['Título']}' removido com sucesso!")
    
    else:
        print("Erro: Livro não encontrado.")

# Listar livros
def listar_todos_livros():
    if not estoque_livros:
        print("Nenhum livro cadastrado.")
    
    else:
        print("Lista de Livros Cadastrados:")
        for livro in estoque_livros:
            print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}, "
                  f"Quantidade: {livro['Quantidade']}, Código: {livro['Código']}")

# Menu do  sistema de gerenciamento de estoque de livros

def biblioteca():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Buscar Livro por Código")
        print("3. Atualizar Estoque de um Livro")
        print("4. Remover Livro do Sistema")
        print("5. Listar Todos os Livros")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            quantidade = int(input("Quantidade em estoque: "))
            codigo = input("Código do livro: ")
            cadastrar_livro(titulo, autor, genero, quantidade, codigo)

        elif opcao == "2":
            codigo = input("Código do livro a ser buscado: ")
            livro = buscar_livro(codigo)
            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Erro: Livro não encontrado.")

        elif opcao == "3":
            codigo = input("Código do livro a ser atualizado: ")
            nova_quantidade = int(input("Nova quantidade em estoque: "))
            atualizar_estoque(codigo, nova_quantidade)

        elif opcao == "4":
            codigo = input("Código do livro a ser removido: ")
            remover_livro(codigo)

        elif opcao == "5":
            listar_todos_livros()

        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
biblioteca()