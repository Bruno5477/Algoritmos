"""
Counting sort:
É um algoritmo de ordenação não-comparativa que é muito eficiente quando quantidade de valores dos 
elementos na lista é pequena. Ele usa uma contagem dos elementos para ordenar, 
o que o torna mais rápido do que os algoritmos de comparação em quando o intervalo de valores é limitado.

Vantagens:
    Desempenho rápido em intervalos pequenos;
    Não depende de comparações;
    Ele é estável.

Desvantagens:
    Ordena apenas numeros inteiros, precisa de uma adaptação para trabalhar com strings;
    Não é eficiente para intervalos grandes;
    Memória extra é necessária para armazenar a lista de contagem.

Passo a passo:
    Começar uma nova lista com o alcance da lista original iniciando com o valor 0 em todos os elementos.
    No incide correspondente ao valor de cada elemento da lista original, é colocado o quanto o valor original se repete na lista.
    Nessa nova lista, fazer a soma do elemeto anterior com o da posição atual e atualizar o valor, repetir esse processo em toda lista.
    Criar nova lista com mesmo tamanho da original.
    Ler lista original de trás para frente e colocar o valor dessa lista na posição definida pelo valor no 
    indice correspondente ao valor original na primeira lista criada.
    Conforme for adicionando nas posições, tirar 1 nos valores correspondentes na primeira lista criada.


"""
def counting_sort(lista):
    # Encontrando o valor máximo da lista
    valor_max = max(lista)
    count = [0] * (valor_max + 1) # Inicializando uma lista de contagem com zeros

    while len(lista) > 0:
        # Removendo o primeiro elemento da lista e o armazenando na variável num
        num = lista.pop(0) 

        # contando a quantidade de vezes que cada número aparece na lista original
        count[num] += 1 

    # construindo a lista ordenada com base nas contagens.
    for i in range(len(count)):
        
        while count[i] > 0:
            lista.append(i)
            count[i] -= 1

    return lista

# Exemplo
lista = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
lista_ordenada = counting_sort(lista)
print("Lista ordenada:", lista_ordenada)
