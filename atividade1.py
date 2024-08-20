# criando a lista vazia que receberá os clientes
clientes = []

#criando a função que adiciona clientes, note que criamos uma lista dentro da própria função para adicionarmos ela na lista clientes
def adicionar_cliente(nome,email,telefone,endereco):
    cliente = [nome,email,telefone,endereco]
    clientes.append(cliente)

#Criando uma função que exibi todos os clientes da lista
def exibir_clientes():
    for cliente in clientes:
        print(f"Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")

#Criando uma função que busca o cliente pelo e-mail e retorna suas informações
def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Cliente encontrado: Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}\n")      
            return #usando o return aqui para encerrar a função
    print(f"Não temos um Cliente registrado com esse o e-mail: {email}.\n")

#Criando a função que remove o cliente pelo email do mesmo
def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print(f"O Cliente com o e-mail {email} foi removido da lista de clientes.\n")
            return #usando o return aqui para encerrar a função      
    print(f"O Cliente com o {email} não foi encontrado.\n")



#criando a função que serve como o menu do sistema criado, onde integramos as funções criadas

def sistema ():
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


#sistema()

adicionar_cliente("Bruno","brunoaalves@gmail","rgrwgwr","ewfwfw")
adicionar_cliente("Nathy","nathy@gmail.com","regergg", "hedghsrg")
exibir_clientes()
buscar_cliente("brunoaalves@gmail")
remover_cliente("nathy@gmail.com")
