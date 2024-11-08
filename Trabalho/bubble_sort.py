def bubble_sort(arr:list) -> list:
    change = True
    n = len(arr)
    while change:
        change = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr

lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
bubble_sort(lista)
print(f'\nLista ordenada: {lista}\n')