def registrar_usuario(nome_arquivo):
    
    try:        
        nome = input("Digite o nome do usuário: ")
        idade = input("Digite a idade do usuário: ")
        email = input("Digite o email do usuário: ")   
        
        if not nome or not idade or not email:
            print("Erro: Todos os campos são obrigatórios.")
            return        
        
        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(f"Nome: {nome}, Idade: {idade}, email: {email}\n")
        
        print("Usuário registrado com sucesso!")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


arquivo_usuarios = "usuarios.txt"
registrar_usuario(arquivo_usuarios)
