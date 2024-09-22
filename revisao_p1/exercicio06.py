dias_da_semana = {
    "Segunda-feira": 0,
    "Terça-feira": 0,
    "Quarta-feira": 0,
    "Quinta-feira": 0,
    "Sexta-feira": 0,
    "Sábado": 0,
    "Domingo": 0
}

for dia in dias_da_semana:
    horas = float(input(f"Insira o número de horas trabalhadas no {dia}: "))
    dias_da_semana[dia] = horas

total_horas = sum(dias_da_semana.values())

print(f"O total de horas na semana foi: {total_horas} horas.")
