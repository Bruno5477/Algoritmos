def triangulo(b,h):
    return (b*h)/2


poligono = input("Qual o poligono que você deseja a área? ")

if poligono == 'triangulo':
    b = int(input('Qual a base desse triângulo? '))
    a = int(input('Qual a altura desse triângulo? '))
    print(triangulo(b,a))
else:
    print('Nome errado')