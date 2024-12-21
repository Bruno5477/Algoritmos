def busca_sequencial(lista, chave):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == chave:
            posicoes.append(i)
    return posicoes

def busca_binaria(lista, chave):
    def busca_binaria_recursiva(lista, chave, inicio, fim, posicoes):
        if inicio > fim:
            return
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            posicoes.append(meio)
            # Verifica elementos à esquerda do meio
            esquerda = meio - 1
            while esquerda >= inicio and lista[esquerda] == chave:
                posicoes.append(esquerda)
                esquerda -= 1
            # Verifica elementos à direita do meio
            direita = meio + 1
            while direita <= fim and lista[direita] == chave:
                posicoes.append(direita)
                direita += 1
        elif lista[meio] < chave:
            busca_binaria_recursiva(lista, chave, meio + 1, fim, posicoes)
        else:
            busca_binaria_recursiva(lista, chave, inicio, meio - 1, posicoes)

    posicoes = []
    busca_binaria_recursiva(lista, chave, 0, len(lista) - 1, posicoes)
    return sorted(posicoes)

# Exemplos de uso
lista = [1, 2, 2, 3, 3, 4, 4, 5]
chave = 4
print(busca_sequencial(lista, chave))  
print(busca_binaria(lista, chave))     