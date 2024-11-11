def potencia(base,exp):
    if exp == 0:
        return 1
    
    else:
        return base * potencia(base,exp -1)

base = int(input("Insira o valor da base: "))
expoente = int(input("Insira o valor do expoente: "))

print(f"O resultado da operação {base} elevado à {expoente} é igual à {potencia(base,expoente)}")