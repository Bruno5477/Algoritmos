alunos = {
    "Bruno": {"Matemática": 10.0, "Português": 8.0, "Ciências": 10.0},
    "Rosonatt": {"Matemática": 6.0, "Português": 8.0, "Ciências": 8.5},
    "Nathy": {"Matemática": 9.5, "Português": 9.5, "Ciências": 9.0},
    "Ryan": {"Matemática": 9.0, "Português": 9.0, "Ciências": 9.5}
}

def consultar_nota(nome:str):
    if nome in alunos:
        print(f"As notas do(a) aluno(a) {nome} foram: ")
        for disciplina, nota in alunos[nome].items():
            print(f"{disciplina} : {nota}")
            
    else:
        print(f"O(A) Aluno(a) {nome} não foi encontrado.")

def atualiza_nota (nome:str, disciplina:str, nota:float):
    if nome in alunos:
        if disciplina in alunos[nome]:

            alunos[nome][disciplina] = nota
            print(f"A nota do Aluno(a) {nome} na disciplina de {disciplina} foi atualizada para: {nota}")
        
        else:
            print(f"A disciplina {disciplina} não teve sua nota lançadada ou não existe na base de dados.")
    
    else:
        print(f"O(A) aluno(a) {nome} não foi encontrado.")



consultar_nota("Bruno")
atualiza_nota("Rosonatt","Matemática", 7.5)