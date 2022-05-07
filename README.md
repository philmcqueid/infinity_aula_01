# infinity_aula_01

### 01 - O que é lógica de programação?
- Lógica de programação é a capacidade de organizar uma sequencia de passos para se chegar a um determinado resuldado.
### 02 - Ir de um ponto da cidade até a sala de aula da infinity?
1 - Sair de casa
2 - Caminhar até o ponto de ônibus
3 - Aguardar o ônibus
4 - Subir no ônibus
5 - Aguardar chegar até o terminal
6 - Pegar outro ônibus
7 - Descer na parada mais próxima da escola
8 - Caminhar até a escola
9 - Entrar na escola

### 03 - Linguágens de programação mais utilizadas 2020, 2021, 2022:
  - 2022: Python - fonte: https://devbugado.com/5-linguagens-programacao-mais-usadas/
  - 2021: Python - fonte: https://www.tecmundo.com.br/mercado/222806-5-linguagens-programacao-usadas-2021.htm
  - 2020: Python - fonte: https://itforum.com.br/noticias/python-domina-ranking-de-linguagens-de-programacao-de-2020/

### 04 - Liste 3 valores para cada tipo de variável:
- 1) Inteiro: Idade, número de residência, senha de fila de espera
- 2) String: Nome, Endereço, Descrição de perfil
- 3) Float: Dinheiro, Altura, Peso
### 05

~~~ # Aula Introdução ao Python

# Esta é uma aula de programação

# Vimos que existem várias linguagens, 

# como

# a linguagem Java!

# A linguagem que estamos utilizando é

# a linguagem Python!

# Nossa Aula é na 

# Infinity

# também conhecida como

# Infinity School.

# Bons códigos!

# Esta Linha será um comentário em breve!
~~~~

# Atividade 6
~~~
num_01 = 10
num_02 = 50

print("O produto de", num_01, "*", num_02, "é:", num_01 * num_02)
~~~
# Atividade 7 - Calcule a média entre 8, 9 e 7
~~~
media = (8 + 9 + 7) / 3

print(f"A média é: {media}. Esta variável é do tipo {type(media).__name__}")
~~~

# Atividade 8 - Peça ao usuário para seu nome e sobrenome e apresente em tela

~~~
user_name = input("Digite seu nome: ")
user_surname = input("Digite seu sobrenome: ")
complete_name = f"{user_name} {user_surname}"
print(f"Seu nome completo é: {complete_name}")
~~~

# Atividade 9 - Peça ao usuário dois números inteiros e apresente a soma dos dois
~~~
int_num_01 = int(input("Número 01: "))
int_num_02 = int(input("Número 02: "))

result = int_num_01 + int_num_02

print(f"A soma de {int_num_01} + {int_num_02} = {result}")
~~~
# Atividade 10 - Refaça o programa das médias, agora com 4 notas, pedindo as notas para o usuário, e, por fim, mostrar o resultado em tela
~~~
nota_01 = int(input("Digite a nota 01: "))
nota_02 = int(input("Digite a nota 02: "))
nota_03 = int(input("Digite a nota 03: "))
nota_04 = int(input("Digite a nota 04: "))
print("\n")

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4

print(f"Sua média final foi: {media}")
~~~


# Atividade 11 - Peça dois números ao usuário, mostre os resultados de uma calculadora básica
~~~
print("\n")  # Apenas para dar espaçamento
number_01 = int(input("Digite o primeiro número: "))
number_02 = int(input("Digite o segundo número: "))
print("\n")  # Apenas para dar espaçamento

adicao = number_01 + number_02
subtracao = number_01 - number_02
multiplicacao = number_01 * number_02
divisao = number_01 / number_02

print(f"O resultado de {number_01} + {number_02} = {adicao}")
print(f"O resultado de {number_01} - {number_02} = {subtracao}")
print(f"O resultado de {number_01} * {number_02} = {multiplicacao}")
print(f"O resultado de {number_01} / {number_02} = {divisao}")
~~~
