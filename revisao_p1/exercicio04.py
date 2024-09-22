pessoas = []

def imprimir_lista(nome:str, idade:int, cidade:str):
    pessoa = [nome, idade, cidade]
    pessoas.append(pessoa)

def exibir_nomes():
     for ident in pessoas:
        print(f"Nome: {ident[0]}, Idade: {ident[1]}, Cidade: {ident[2]}")


imprimir_lista("Bruno",27,"Saquarema")
imprimir_lista("Rosonatt",29,"Saquarema")



exibir_nomes()