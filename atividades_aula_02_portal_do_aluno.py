"""Atividade 01 — Solicite um número ao usuário e mostre se o número é positivo ou negativo."""

# Número inserido pelo usuário
chosen_number = int(input("Escolha um número: "))

if chosen_number > 0:
    print(f"O número {chosen_number} é positivo!")
else:
    print(f"O número {chosen_number} é negativo!")

"""
Atividade 02 — A cancela de um estabelecimento, neste momento de pandemia funciona dependendo da temperatura aferida 
e registrada pelo recepcionista do local. É preciso criar um algoritmo para liberar ou não cancela dependendo da 
temperatura corporal. Com um medidor o recepcionista irá aferir e registrar no sistema e o algoritmo deverá liberar 
caso a temperatura seja <= 37 e não liberar caso a temperatura seja maior que 37º.
A cancela só recebe True ou False (True para liberar e False para bloquear).
"""
# Temperatura registrada pela cancela
registered_temperature = int(input("Temperatura do cliente: "))

# conversão da temperatura para booleano
allowed_entry = registered_temperature <= 37

if allowed_entry:
    print(f"Temperatura registrada {registered_temperature}°. Entrada permitida!")
else:
    print(f"Temperatura registrada {registered_temperature}°. Entrada negada!")

"""
Atividade 03 — Receber do usuário a quantidade de respiradores e a porcentagem de ocupação de 5 hospitais em Salvador, 
caso algum 
desses hospitais tenham menos que 50 respiradores e a taxa ocupacional esteja maior que 60%, serão adicionados mais 5. 
"""
hospitals = [

]

# Adiciona a quantidade de respiradores e a taxa de ocupação
for i in range(1, 6):
    print(f"Hospital {i}:")
    number_of_respirators = int(input("Quantidade de respiradores: "))
    occupation = float(int(input("Taxa de ocupação: ")) / 100)
print("\n")
hospitals.append({"hospital": i, "occupation": occupation, "number_of_respirators": number_of_respirators})

# Verifica se é necessário adicionar mais respiradores
for hospital in hospitals:
    if hospital["number_of_respirators"] < 50 and hospital["occupation"] > 0.6:
        hospital["number_of_respirators"] += 5

# Imprime os dados finais sobre cada hospital
for hospital in hospitals:
    print(f"Hospital: {hospital['hospital']}\n"
          f"taxa de ocupação: {hospital['occupation'] * 100}%\n"
          f"Respiradores: {hospital['number_of_respirators']}")
    print("\n")

"""
Atividade 04 — A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 
grupos de indústrias que são altamente poluentes do meio ambiente. 
O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as 
indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as 
indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos 
devem ser notificados a paralisarem suas atividades. Faça um algoritmo que leia o
índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas
"""
