def count_chaves(lista, X, Y):
    count = 0
    for num in lista:
        if X <= num <= Y:
            count += 1
    return count

# Exemplo de uso
sorted_list = [1, 3, 5, 7, 9, 11, 13]
X = 4
Y = 10
print(count_chaves(sorted_list, X, Y))  # Saída esperada: 3