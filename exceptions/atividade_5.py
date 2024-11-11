"""Simulação de transações: Crie um programa que simule uma transferência
bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o
saldo seja insuficiente, levante uma exceção do tipo ValueError com a
mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o
usuário."""

def trans_bancaria():
    try:
        saldo = float(input(f"Digite o saldo da conta: "))
        valor_transferido = float(input(f"Digite o valor da transferência: "))
        
        if valor_transferido > saldo:
            raise ValueError(f"Saldo insuficiente")
        
        novo_saldo = saldo - valor_transferido
        print(f"Transferência realizada com sucesso. Novo saldo: R$ {novo_saldo:.2f}")

    except ValueError as e:
        if str(e) == "Saldo insuficiente":
            print(f"{str(e)}. Não foi possível realizar a transferência.")
        else:
            print(f"Por favor, insira valores numéricos válidos.")

trans_bancaria()