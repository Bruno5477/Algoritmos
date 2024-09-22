numero = []

def lista_sem_dupli(n:int):
    numero_sem_duplicata = []
    for i in range(n):
        num = int(input(f"Insira o {i+1}° número da lista: "))
        numero.append(num)
    
    numero_sem_duplicata = list(set(numero))

    return numero_sem_duplicata

resultado = lista_sem_dupli(5)
print(f"A lista sem números duplicados {resultado}")