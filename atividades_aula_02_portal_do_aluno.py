"""Atividade 01 — Solicite um número ao usuário e mostre se o número é positivo ou negativo."""

# # Número inserido pelo usuário
# chosen_number = int(input("Escolha um número: "))
#
# if chosen_number > 0:
#     print(f"O número {chosen_number} é positivo!")
# else:
#     print(f"O número {chosen_number} é negativo!")

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


