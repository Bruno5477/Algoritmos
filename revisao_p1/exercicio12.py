produto_preco = {
    "Notebook": 4500.00,
    "Smartphone": 2100.00,
    "Fones de Ouvido": 200.00,
    "Teclado": 150.00,
    "Monitor": 800.00,
    "Processador": 1000.00,
    "Gabinete":350.00,
    "Mouse": 130.00
}

def produto_mais_caro(lista_produto:dict):
    mais_caro = max(lista_produto, key= lista_produto.get)

    print(f"O produto mais caro da loja é o {mais_caro}.")

produto_mais_caro(produto_preco)
