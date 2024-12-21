def busca_binaria_variada(lista, chave):
    esquerda, direita = 0, len(lista)
    
    while esquerda < direita:
        meio = (esquerda + direita) // 2
        if lista[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio
    
    return esquerda

# Exemplo de uso
lista = [1, 3, 5, 7, 9]
chave = 6
k = busca_binaria_variada(lista, chave)
print(f"Posição para inserir a chave {chave}: {k}")