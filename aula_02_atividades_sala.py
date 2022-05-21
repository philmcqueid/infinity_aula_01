# # Atividade 1
#
# user_chosen_number = int(input("Digite um número: "))
#
# if user_chosen_number == 0:
#     print(f"O número {user_chosen_number} não é positivo nem negativo")
# elif user_chosen_number > 0:
#     print(f"O número {user_chosen_number} é positivo")
# else:
#     print(f"O número {user_chosen_number} é negativo")

# # Atividade 2
#
# detected_speed = int(input("Qual a velocidade atual em Km/h: "))
#
# allowed_speed = detected_speed <= 60
#
# if allowed_speed:
#     print(f"A velocidade atual é de {detected_speed}Km/h. VELOCIDADE PERMITIDA!")
# elif 60 < detected_speed < 80:
#     print(f"A velocidade atual é de {detected_speed}Km/h. ALTA VELOCIDADE!")
# elif 80 < detected_speed < 120:
#     print(f"A velocidade atual é de {detected_speed}Km/h. MUITO RÁPIDO!")
# else:
#     print(f"A velocidade atual está a cima de 120Km/h. ALTO RISCO!")

# # Atividade 3
# import math
#
# user_weight = float(input("Qual seu peso em kg: "))
# user_height = float(input("Qual sua altura m: "))
#
# user_imc = user_weight / math.pow(user_height, 2)
#
# if user_imc <= 18.5:
#     print("abaixo do peso")
# elif 18.5 < user_imc <= 24.9:
#     print("normal")
# elif 25 <= user_imc <= 29.9:
#     print("sobrepeso")
# elif 30 <= user_imc <= 39.9:
#     print("obesidade tipo I")
# else:
#     print("obesidade ")

# # Atividade 4
# guess = int(input("Qual o palpite: "))
# secret_number = 43
#
# if guess == secret_number:
#     print(f"Os número são iguais")
# elif guess > secret_number:
#     print(f"O número escolhido é maior do que o número escondido")
# else:
#     print(f"O número escolhido é menor do que o número escondido")

# # Atividade 5
# current_temperature = int(input("Temperatura atual: "))
#
# if current_temperature <= 37:
#     print("Temperatura NORMAL")
# elif 37 < current_temperature <= 37.8:
#     print(f"Temperatura atual {current_temperature}. FEBRIL")
# elif 37.5 < current_temperature <= 38.5:
#     print(f"Temperatura atual {current_temperature}. FEBRE LEVE")
# elif 38.5 < current_temperature <= 39.4:
#     print(f"Temperatura atual {current_temperature}. FEBRE MODERADA")
# else:
#     print(f"Temperatura atual {current_temperature}. FEBRE GRAVE")

login = input("Login: ").upper().strip()
password = input("Senha: ")

if login == "INFINITY" and password == "school":
    print("Login feito com sucesso!")
else:
    print("Login ou senha inválidos!")
