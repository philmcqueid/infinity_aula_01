# Início
"""01 — Faça um Programa que converta metros para centímetros"""
meters = float(input("Converta 'Metro' em 'Centímetros'\nQuantos metros deseja converter: "))
meters_to_centimeters = meters * 100
print(f"{meters}m é igual a {meters_to_centimeters}cm")

"""02 — Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

raio = float(input("Qual o valor do raio: "))
PI = 3.14
circle_area = PI + raio ** 2
print(f"A área total do círculo é {circle_area}")


"""03 — Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""
import math

raio = float(input("Qual o valor do raio: "))
PI = round(math.pi, 2)
circle_area = PI + raio ** 2
print(f"A área total do círculo é {circle_area}")

"""04 — Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus 
Celsius. C = 5 * ((F-32) / 9)"""
fahrenheit_temperature = int(input("Temperatura em Fahrenheit: "))
fahrenheit_to_celsius = round((fahrenheit_temperature - 32) * 5 / 9)
print(f"{fahrenheit_temperature}°F é igual a {fahrenheit_to_celsius}°C")


"""05 — Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""
celsius_temperature = int(input("Temperatura em celsius: "))
celsius_to_fahrenheit = round((celsius_temperature * 9 / 5) + 32)
print(f"{celsius_temperature}°C é igual a {celsius_to_fahrenheit}°F")

"""06 — Imprima um número em tela"""
print(100)

"""07 —  Crie uma variável com um número inteiro, imprima a variável"""
number = 100
print(number)

"""08 —  Peça ao usuário um número e depois imprima o número em tela"""
user_chosen_number = int(input("Digite um número: "))
print(f"Seu número foi: {user_chosen_number}")

"""09 —  Faça um Programa que peça dois números e imprima a soma."""
print("Some dois números\n")
number_01 = int(input("Primeiro número: "))
number_02 = int(input("Segundo número: "))
soma = number_01 + number_02
print(f"{number_01} + {number_02} = {soma}")

"""10 —  Faça um Programa que peça as 4 notas e calcule a média. Ao final do programa, mostre todas 
as notas e por fim, a média."""

nota_01 = float(input("Nota 01: "))
nota_02 = float(input("Nota 02: "))
nota_03 = float(input("Nota 03: "))
nota_04 = float(input("Nota 04: "))

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4

print(f"Nota 1: {nota_01}\nNota 2: {nota_02}\nNota 3: {nota_03}\nNota 4: {nota_04}\nMédia final: {media}")

"""
11 — Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
compradas e o preço total.
"""
# (Quantidade) metros quadrados desejados
amount_square_meters = int(input("Quantos metros quadrados: "))
coverage_per_liter = 3
# Quantidade de litros necessários
liters_needed = amount_square_meters / coverage_per_liter
lata_de_tinta = 18
valor_lata_tinta = 80.0

print(liters_needed)

"""12 — Peça ao usuário uma velocidade em Km/h (Quilômetro por hora) e converta para M/s (Metros por segundo). A 
fórmula utilizada é Km = M * 3.6 (K é a velocidade em Km/h e M a velocidade em M/s)"""

velocity = float(input("Escolha uma velocidade em km/h: "))

speed_in_meters_per_second = round(velocity / 3.6, 2)

print(f"{velocity}km/h = {speed_in_meters_per_second}m/s")

"""13 — Altere o programa acima para que a velocidade solicitada ao usuário seja em M/s, e então, converta para Km/h."""

velocity = float(input("Escolha uma velocidade em m/s: "))

speed_in_km_per_hour = round(velocity * 3.6, 2)

print(f"{velocity}m/s = {speed_in_km_per_hour}km/h")

"""14 — Peça três número inteiros e imprima a soma entre eles."""

number_01 = int(input("Escolha um número: "))
number_02 = int(input("Escolha outro número: "))
number_03 = int(input("Escolha mais um número: "))

soma = number_01 + number_02 + number_03

print(f"A soma entre {number_01}, {number_02} e {number_03} é igual {soma}")

"""15 — Um funcionário recebeu um aumento de 25% no seu salário. Peça o salário atual e mostre em tela o 
salário com o aumento."""


"""16 — Um prêmio da loteria de R$ 540.000 será dividido entre três pessoas. Informe o 
valor recebido por cada pessoa."""

prize_value = 540000
print(f"Os vencedores receberão cada um, R$ {prize_value / 3}.")

"""17 — O prêmio acima foi entregue à três ganhadores de um concurso. O primeiro receberá: 47% 
O segundo receberá: 31% O terceiro receberá o restante Calcule e mostre em tela o valor recebido por cada ganhador."""

prize = 540000

first_winner_value = prize * 0.47
second_winner_value = prize * 0.31
third_winner_value = prize - (first_winner_value + second_winner_value)

print(f"1º Prêmio: R$ {first_winner_value}.\n2º Prêmio: R$ {second_winner_value}.\n3º Prêmio: R$ {third_winner_value}.")

"""18 — Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:"""
int_number_01 = int(input("Escolha um número inteiro: "))
int_number_02 = int(input("Escolha outro número inteiro: "))
real_number = float(input("Escolha um número real: "))

# o produto do dobro do primeiro com metade do segundo.
produto = (int_number_01 * 2) * (int_number_02 / 2)
print(f"Produto: {produto}")

# a soma do triplo do primeiro com o terceiro.
soma = (int_number_01 * 3) + real_number
print(f"Soma: {produto}")

# o terceiro elevado ao cubo.
terceiro_ao_cubo = real_number ** 3
print(f"Terceiro elevado ao cubo: {terceiro_ao_cubo}")

"""19 — Peça três valores (um int, um float, uma string) ao usuário e ao final, mostre em 
tela o valor e o TIPO de cada um."""

int_number = int(input("Escolha um número: "))
float_number = float(input("Escolha outro número: "))
user_string = str(input("Escolha uma palavra: "))

print(f"{type(int_number)}\n{type(float_number)}\n{type(user_string)}")

"""20 — Mostre em tela o valor da divisão de um número inteiro digitado pelo usuário por dois. 
OBS: A operação é por módulo: número MÓDULO 2."""

user_chosen_number = int(input("Escolha um número: "))

print(f"Resultado: {user_chosen_number % 2}")
