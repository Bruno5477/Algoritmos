frutas = []
for i in range(4):
    item = input(f"Insira a {i +1}º fruta: ").lower()
    frutas.append(item)

tem_fruta = input("Qual a fruta você quer saber se tem na lista? ").lower()

if tem_fruta in frutas:
    print(f"A fruta {tem_fruta} está na lista de frutas.")
else:
    print(f"A {tem_fruta} não está na lista de frutas.")