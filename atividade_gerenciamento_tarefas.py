# Inicializa uma lista vazia para armazenar as tarefas
lista_tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    
    if lista_tarefas:
        novo_id = max(tarefa["id"] for tarefa in lista_tarefas) + 1
    else:
        novo_id = 1

    
    nova_tarefa = {
        "id": novo_id,
        "descricao": descricao,
        "status": status,
        "prioridade": prioridade
    }

    
    lista_tarefas.append(nova_tarefa)

# Função para visualizar todas as tarefas
def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa adicionada ainda.")
        return
    
    for tarefa in lista_tarefas:
        print(f'ID: {tarefa["id"]}, Descrição: {tarefa["descricao"]}, Status: {tarefa["status"]}, Prioridade: {tarefa["prioridade"]}')

# Função para filtrar tarefas por status ou prioridade
def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = [
        tarefa for tarefa in lista_tarefas
        if (status is None or tarefa["status"] == status) and
           (prioridade is None or tarefa["prioridade"] == prioridade)
    ]
    return tarefas_filtradas



# Adicionando algumas tarefas
adicionar_tarefa(lista_tarefas, "Implementar API", "pendente", "alta")
adicionar_tarefa(lista_tarefas, "Testar módulo de login", "em andamento", "média")
adicionar_tarefa(lista_tarefas, "Documentar funções", "concluída", "baixa")

# Visualizando todas as tarefas
print("Todas as tarefas:")
visualizar_tarefas(lista_tarefas)

# Filtrando tarefas por status
print("\nTarefas pendentes:")
tarefas_pendentes = filtrar_tarefas(lista_tarefas, status="pendente")
visualizar_tarefas(tarefas_pendentes)

# Filtrando tarefas por prioridade
print("\nTarefas de prioridade alta:")
tarefas_alta_prioridade = filtrar_tarefas(lista_tarefas, prioridade="alta")
visualizar_tarefas(tarefas_alta_prioridade)
