numeros = [1, 2, 4, 5, 10]

def multiplicar_lista(lista:list, multiplicador = 1):
    lista_multiplicada = [numero * multiplicador for numero in lista]
    
    return lista_multiplicada

nova_lista = multiplicar_lista(numeros, 2)
nova_lista2 = multiplicar_lista(numeros)

print(f"A lista de números {numeros} multiplica por 2 é igual à: \n{nova_lista}")
print(f"A lista de números {numeros} multiplica por 1 é igual à: \n{nova_lista2}")