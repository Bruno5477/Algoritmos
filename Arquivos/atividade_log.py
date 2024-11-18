from datetime import datetime

def registrar_evento():

    descricao = input("Digite uma breve descrição sobre o evento: ")
    tempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("sistema_log.txt", "a") as arquivo_log:
            arquivo_log.write(f"{tempo} - Evento: {descricao}\n")
        print("Evento registrado com sucesso")
    
    except Exception as e:
        print(f"Erro ao registrar o evento: {e}")


def visualizar_log():

    try:
        with open("sistema_log.txt") as arquivo_log:
            log = arquivo_log.read()

            if log:
                print("\nEventos registrados: ")
                print(log)
            
            else:
                print("\nO registro de eventos está vázio.")
    
    except FileNotFoundError:
        print("O arquvivo de log não foi encontrado. Nenhum evento foi registrado até o momento.")
    
    except Exception as e:
        print(f"Erro ao visualizar o log: {e}")


def menu():

    while True:
        print("\nEscolha uma opção:")
        print("1. Registrar um novo evento")
        print("2. Visualizar o log completo")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            registrar_evento()
        elif opcao == "2":
            visualizar_log()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()