dicionario_alunos = {}
def notas_aluno(info:list):
    

    for nome, nota in info:
        dicionario_alunos[nome] = nota
    return dicionario_alunos

def consultar(dicionario:dict, nome:str):
    if nome in dicionario:
        print(f"{nome} tema a nota igual à : {dicionario[nome]}")
    else: 
        print(f"O Aluno(a) {nome} não foi encontrado.")

    

def atualizar_nota(dicionario: dict, nome: str, nota:float):
    if nome in dicionario:
        dicionario[nome] = nota
        print(f" A nota de {nome} foi atualizada para: {nota}")
    else:
        print(f"O aluno(a) {nome} não foi encontrado.")


alunos = [("Bruno", 9.5), ("Kuze", 10), ("Alya", 10)]

print(notas_aluno(alunos))

consultar(dicionario_alunos, "Alya")
consultar(dicionario_alunos, "Rosonatt")

atualizar_nota(dicionario_alunos,"Bruno", 10)

