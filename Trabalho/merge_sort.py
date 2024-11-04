"""
Merge Sort: 

É um algoritmo de ordenação que consiste em dividir uma estrutura em subconjuntos e ir 
aplicando a ordenação nos elementos que foram extraídos da estrutura originaria, depois da 
ordenação é feito a união (merge) dos subconjuntos em um conjunto final ordenado.

Vantagens :
    Mais eficiente que os algoritmos "selection", "bubble" e o "insertion";
    Ideal para listas grandes;
    Ele é estável pois mantém a ordem dos elementos iguais

Desvantagens:
    Desempenho para listas pequenas é menos eficientes que outros, como o insertion;
    Não é muito amigavél para iniciantes;
    uso extra de memória, já que cria cópias da lista para fazer a ordenação e mesclagem.

 Passo a passo:
    Dividir a lista em 2 sublistas.
    Dividir as sublistas em mais 2 sublistas cada.
    Repetir esse passo até o menor tamanho.
    Juntar duas sublistas de menor tamanho de forma ordenada.
    Repetir esse passo com as restantes.
    Depois juntar duas sublistas resultantes de forma ordenada novamente, comparando os primeiros elementos e ordenando, até o final.
    Repetir esse processo até que reste apenas uma lista já ordenada.
"""

def merge_sort(lista):

    # Caso base da recursão, se a lista tiver 0 ou 1 elemento, ela já está ordenada.
    if len(lista) <= 1:
        return lista
    
    else:

        # Dividindo a lista em duas metades
        mid = len(lista) // 2
        metade_1 = merge_sort(lista[:mid])
        metade_2 = merge_sort(lista[mid:])

        # unindo as duas metades ordenadas
        return merge(metade_1, metade_2)

def merge(esquerda, direita):
    lista_ordenada = []
    i = 0
    j = 0

    # Comparando elementos de ambas as metades e adicionando o menor a lista ordenada
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1

    # Adiciona os elementos restantes, se houver algum
    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])

    return lista_ordenada

# Exemplo 
lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)
