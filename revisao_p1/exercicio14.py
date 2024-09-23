estoque_loja = {
    "Notebook": 120,
    "Smartphone": 5,
    "Fones de Ouvido": 20,
    "Teclado": 15,
    "Monitor": 8,
    "Processador": 10,
    "Gabinete":10,
    "Mouse": 13
}

def atualizar_estoque(estoque_produtos:dict, produto:str, quantidade: int):
    if produto in estoque_produtos:
        quantidade_estoque = estoque_produtos[produto]
        if quantidade <= quantidade_estoque:
            estoque_produtos[produto] -= quantidade
            print(f"Venda realizada com sucesso: {quantidade} unidades de {produto} vendidas. \nEstoque atualizado com {estoque_produtos[produto]} unidades restantes.")
        
        else:
            print(f"Quantidade vendida excede o número de unidades do {produto} disponíveis em nosso estoque.")
            print(f"Estoque disponível de {produto}: {estoque_produtos[produto]} unidades.")
    
    else:
        print(f"Produto '{produto}' não foi encontrado em nosso estoque.")

atualizar_estoque(estoque_loja, "Notebook", 5)
atualizar_estoque(estoque_loja, "Smartphone", 6)
atualizar_estoque(estoque_loja, "Cadeira", 6)
            
            