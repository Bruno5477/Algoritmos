def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)  + fibonacci(n-2)

num = int(input("Insira o número do termo da sequência de Fibonacci desejada: "))

print(f"O {num}-ésimo termo da sequência de Fibonacci é: {fibonacci(num)}")

