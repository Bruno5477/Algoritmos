def busca_binaria(arr, alvo):
    esquerda, direita = 0, len(arr) - 1

    while esquerda <= direita:
        meio = esquerda + (direita - esquerda) // 2

        # Verifica se o alvo está presente no meio
        if arr[meio] == alvo:
            return meio
        # Se o alvo for maior, ignora a metade esquerda
        elif arr[meio] < alvo:
            esquerda = meio + 1
        # Se o alvo for menor, ignora a metade direita
        else:
            direita = meio - 1

    # O alvo não está presente no array
    return -1

# Exemplo de uso
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    alvo = 10

    resultado = busca_binaria(arr, alvo)

    if resultado != -1:
        print(f"Elemento está presente no índice {resultado}")
    else:
        print("Elemento não está presente no array")