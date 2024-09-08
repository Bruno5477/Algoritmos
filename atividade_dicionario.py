# Iniciando um dicionário vazio
clientes = {}  

#Usamos o email como chave,assim não precisamos percorrer toda a lista
def adicionar_cliente(nome, email, telefone, endereco):
    clientes[email] = {'nome': nome, 'telefone': telefone, 'endereco': endereco}

def exibir_clientes():
    for email, info in clientes.items():
        print(f"Nome: {info['nome']}, E-mail: {email}, Telefone: {info['telefone']}, Endereço: {info['endereco']}")

def buscar_cliente(email):
    if email in clientes:
        cliente = clientes[email]
        print(f"Cliente encontrado: Nome: {cliente['nome']}, E-mail: {email}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}\n")
    else:
        print(f"Não temos um Cliente registrado com esse o e-mail: {email}.\n")

def remover_cliente(email):
    if email in clientes:
        del clientes[email]
        print(f"O Cliente com o e-mail {email} foi removido da lista de clientes.\n")
    else:
        print(f"O Cliente com o {email} não foi encontrado.\n")

#criando um menu interativo
def sistema():
    while True:
        print("Escolha a opção desejada:")
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Buscar Cliente por e-mail")
        print("4. Remover Cliente por e-mail")
        print("5. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            adicionar_cliente(nome, email, telefone, endereco)
        
        elif opcao == '2':
            exibir_clientes()
        
        elif opcao == '3':
            email = input("Digite o e-mail do cliente: ")
            buscar_cliente(email)
        
        elif opcao == '4':
            email = input("Digite o e-mail do cliente a ser removido: ")
            remover_cliente(email)
        
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.\n")

sistema()
