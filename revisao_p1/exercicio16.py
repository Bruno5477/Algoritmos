"""
Lista ordenada: A busca binária só funciona em listas ordenadas.
A busca binária começa comparando um elemento no meio da lista com o valor escolhido. 
Se o valor de destino corresponder ao elemento, sua posição na matriz será retornada. 
Se o valor de destino for menor que o elemento, a pesquisa continua na metade inferior da matriz.
Se o valor de destino for maior que o elemento, a pesquisa continua na metade superior da matriz
 """
def busca_binaria_recursiva(lista:license, chave:int, inicio:int, fim:int):
  if inicio > fim:
    return -1 

  meio = (inicio + fim) // 2

  if lista[meio] == chave:
    return meio
  elif lista[meio] < chave:
    return busca_binaria_recursiva(lista, chave, meio + 1, fim)
  else:
    return busca_binaria_recursiva(lista, chave, inicio, meio - 1)


minha_lista = [1, 5, 15, 20, 24, 45, 67, 76, 78, 100]
resultado = busca_binaria_recursiva(minha_lista, 24, 0, len(minha_lista) - 1)

if resultado == -1:
    print('\nChave não encontrada.\n')
else:
    print(f'\nIndice: {resultado}\n') 