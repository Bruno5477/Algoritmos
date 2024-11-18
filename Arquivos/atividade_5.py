def adicionar_frase (nome_arquivo):

    try:
        frase = input("Digite uma frase para ser adicionada ao arquivo: ")

        with open(nome_arquivo, "a", encoding="UTF-8") as arquivo:
            arquivo.write(frase + "\n")

        print(f"A frase foi adicionada com sucesso ao arquivo '{nome_arquivo}'.")
    
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

arquivo = "anotacoes.txt"

adicionar_frase(arquivo)