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

def verificar_estoque(produto:str):
    if produto in estoque_loja:
        unidades = estoque_loja[produto]
    
        if unidades > 0 :
            print(f"O produto '{produto}' está disponível e temos {unidades} unidades no estoque. ")
        else:    
            print(f"O produto '{produto}' não está disponível no estoque. ")
    else:
        print(f"O produto '{produto}' não foi encontrado no estoque.")

verificar_estoque("Teclado")
verificar_estoque("Cooler")

