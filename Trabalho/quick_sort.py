"""
Quick sort:
Algoritmo para ordenar uma lista com base em um elementos aleatório (pivo) dessa lista.
O Quicksort utiliza a estratégia de “dividir para conquistar”, onde ele divide a lista em 
sub-listas menores, ordena essas sub-listas e, em seguida, as combina para obter a 
lista final ordenada.

Vantagens :
    É eficiente em relação a outros algoritmos de ordenação, como o Bubble Sort e o Insertion Sort;
    É um algoritmo in-place, ou seja, não requer espaço adicional para realizar a ordenação;
    Tem uma complexidade média, o tornando muito rápido em conjuntos grandes.

Desvantagens:
    Não é um algoritmo estável, pois permite que elementos iguais troquem de posições relativas durante a sua execução 
    O desempenho do algoritmo é muito sensível a escolha do pivô.
    Não funciona quando tem elementos repetidos.

Passo a passo:
    Definir um elemento como pivo.
    Verificar cada elemento da lista.
    Passa elementos maiores que o pivo para direita e os menores para a esquerda, gravando a posição entre eles.
    No final trocar a posição do pivo para essa posição intermediária.
    Repetir todo o processo anterior para as sublistas dos menores e para a dos maiores, 
    até que o tamanho das sublistas seja de 1 elemento.

"""

def quick_sort(arr):
    # Caso base da recursão, se a lista tiver 0 ou 1 elemento, ela já está ordenada.
    if len(arr) <= 1:
        return arr
    
    else:
        # Escolhendo o pivô, nesse caso será o último elemento
        pivo = arr[-1]

        # Elementos menores ou iguais ao pivô
        esquerda = [x for x in arr[:-1] if x < pivo]  
        
        # Elementos maiores que o pivô
        direita = [x for x in arr[:-1] if x > pivo]  
        
        # Elementos Iguais ao pivô
        iguais = [x for x in lista if x == pivo]

        # Aplicando a função recursivamente e combinando os resultados
        return quick_sort(esquerda) + iguais + quick_sort(direita)

# Exemplo 
lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
lista_ordenada = quick_sort(lista)
print(f"\nLista não ordenada: {lista} \nLista ordenado: {lista_ordenada}\n")
