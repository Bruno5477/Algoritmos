"""
Radix Sort:
É um algoritmo de ordenação não-comparativa que funciona bem em listas de números inteiros ou
em listas de strings de tamanho fixo. Ele ordena os dados a partir dos dígitos individuais, 
começando do dígito menos significativo (ordenando primeiro pela unidade, depois pela dezena, etc.)

Vantagens:
    Funciona tanto com números quanto com string;
    Não Depende de Comparações;
    É um dos algoritmos mais eficientes.

Desvantagens:
    Pode Ser Ineficiente para Números com Muitos Dígitos;
    Utiliza Memória Extra;
    Não é muito versátil (Limitado a inteiros e strings de comprimento fixo.)

Passo a passo:
    Encontrar o valor máximo.
    Inicializar buckets.
    Agrupar por dígitos.
    Repetir passos até que esteja ordenado.
"""
def radix_sort(lista, base:int = 10):
    
    exp = 1 # iniciando o dígito das unidades
    max_valor = max(lista)
    

    while max_valor // exp > 0:

        # Criando os buckets para a base escolhida
        buckets = [[] for _ in range(base)]

        # Distribuindo os elementos nos buckets com base no dígito atual
        for valor in lista:
            index = (valor // exp) % base # Calculando o índice do bucket para o dígito atual. 
            buckets[index].append(valor)

        # Junta os buckets de volta em uma lista ordenada
        lista = [num for bucket in buckets for num in bucket]

        # Passa para o próxima unidade  (dezenas, centenas, etc.)
        exp *= base

    return lista


lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
lista_ordenada = radix_sort(lista)
print(f"\nLista não ordenada: {lista} \nLista ordenado: {lista_ordenada}\n")