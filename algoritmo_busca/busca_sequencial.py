def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Exemplo de uso
lista = [10, 20, 30, 40, 50]
elemento = 30
resultado = busca_sequencial(lista, elemento)

if resultado != -1:
    print(f'Elemento encontrado na posição: {resultado}')
else:
    print('Elemento não encontrado na lista')