# Atividade 01 — Calcular o IMC:

weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))

imc = weight / (height ** 2)

print(f"Seu imc é: {round(imc, 2)}")

# Atividade 02 — Transformar uma temperatura de Fahrenheit para Celsius:
print("Conversor de temperatura Celsius para Fahrenheit")
temperature_in_celsius = int(input("Qual tempera deseja converter: "))

temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32

print(f"{temperature_in_celsius}° celsius é igual a {temperature_in_fahrenheit}° Fahrenheit")

# Atividade 03 — Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a
# área do retângulo (base*altura).
print("Calcular a área interna de um retângulo")
base = int(input("Qual o valor da base do retângulo: "))
height = int(input("Qual o valor da altura do retângulo: "))

area = base * height
print(f"A área toral do retângulo é de {area} m²")

# Atividade 04 — Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos em
# branco, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


number_of_voters = int(input("Qual a quantidade de eleitores: "))
valid_votes = int(input("Qual a quantidade de votos válidos: "))
blank_votes = int(input("Qual a quantidade de votos em branco: "))
null_votes = int(input("Qual a quantidade de votos nulos: "))

total_votes = valid_votes + blank_votes + null_votes

percent_valid_votes = round(valid_votes * 100 / number_of_voters, 2)
percent_blank_votes = round(blank_votes * 100 / number_of_voters, 2)
percent_null_votes = round(null_votes * 100 / number_of_voters, 2)

no_voters = number_of_voters - total_votes

print(f"\nTotal de eleitores: {number_of_voters}")
print(f"{percent_valid_votes}% dos votos foram válidos.")
print(f"{percent_blank_votes}% dos eleitores votaram em branco")
print(f"{percent_null_votes}% dos eleitores votaram nulo\n")
print(f"Ao todos {no_voters} não votaram. Representam {round(no_voters * 100 / number_of_voters, 2)}% da população")


# Atividade 05 — Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
# A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que
# está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis.

a = 10
b = 20

print(f"Valor de A: {a}\nValor de B: {b}\n")

c = a
a = b
b = c

print(f"Valor de A: {a}\nValor de B: {b}")

# Atividade 05 — O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28%
# e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo
# final ao consumidor.

custo_da_fabrica = int(input("Qual o valor do veículo: R$ "))
percentual_distribuidor = 0.25
impostos = 0.45

custo_final_do_carro = custo_da_fabrica + (custo_da_fabrica * percentual_distribuidor) + (custo_da_fabrica + impostos)

print(f"O valor final do seu veículo é: R$ {custo_final_do_carro}")
