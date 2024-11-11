def palindromo_recursivo(string):
    if len(string) <= 1:
        return True
    
    elif string[0] == string[-1]:
        return palindromo_recursivo(string[1:-1])
    
    else:
        return False
    
palavra = "arara"

palavra2 = "Futebol"


if palindromo_recursivo(palavra):
    print(f"A string '{palavra}' é um palíndromo.")
else:
    print(f"A string '{palavra}' não é um palíndromo.")

if palindromo_recursivo(palavra2):
    print(f"A string '{palavra2}' é um palíndromo.")
else:
    print(f"A string '{palavra2}' não é um palíndromo.")


