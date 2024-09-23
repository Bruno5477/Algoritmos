alunos =[
    {"Nome": "Bruno", "notas": [10.0, 8.0, 10.0]},
    {"Nome": "Rosonatt", "notas": [7.5, 8.0, 10.0]},
    {"Nome": "Nathy", "notas": [9.5, 9.5, 10.0]},
    {"Nome": "Ryan", "notas": [9.0, 9.5, 10.0]},
]

def media_alunos(lista_alunos: list):
    medias = {}

    for aluno in lista_alunos:
        nome = aluno["Nome"]
        notas = aluno["notas"]
        media = round(sum(notas)/len(notas),2)
        medias[nome] = media

    return medias



print(f"A média dos alunos: {media_alunos(alunos)}")