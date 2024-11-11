def cont_digitos(n):
    if abs(n) < 10:
        return 1
    else:
        return 1 + cont_digitos(n // 10)
    
numero = 27
numero2 = 8
resultado = cont_digitos(numero)
resultado2 = cont_digitos(numero2)
print(f"O número {numero} tem {resultado} dígitos.")
print(f"O número {numero2} tem {resultado2} dígitos.")