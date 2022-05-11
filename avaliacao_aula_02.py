"""Prova"""
print("\nDigite o dia e o mês que você faz aniversário para descobrir qual se signo!")
day = int(input("Dia (Ex: 1, 2, 3...): "))
month = input("Mês (Ex: Janeiro, Fevereiro...): ").lower()

if day >= 21 and month == "março" or day <= 20 and month == "abril":
    print("Você é do signo de áries")
elif day >= 21 and month == "abril" or day <= 20 and month == "maio":
    print("Você é do signo de touro")
elif day >= 21 and month == "maio" or day <= 20 and month == "junho":
    print("Você é do signo de gêmeos")
elif day >= 21 and month == "junho" or day <= 22 and month == "julho":
    print("Você é do signo de câncer")
elif day >= 23 and month == "julho" or day <= 22 and month == "agosto":
    print("Você é do signo de leão")
elif day >= 23 and month == "agosto" or day <= 22 and month == "setembro":
    print("Você é do signo de virgem")
elif day >= 23 and month == "setembro" or day <= 22 and month == "outubro":
    print("Você é do signo de libra")
elif day >= 23 and month == "outubro" or day <= 21 and month == "novembro":
    print("Você é do signo de escorpião")
elif day >= 22 and month == "novembro" or day <= 21 and month == "dezembro":
    print("Você é do signo de sagitário")
elif day >= 22 and month == "dezembro" or day <= 20 and month == "janeiro":
    print("Você é do signo de capricórnio")
elif day >= 21 and month == "janeiro" or day <= 18 and month == "fevereiro":
    print("Você é do signo de aquário")
elif day >= 19 and month == "fevereiro" or day <= 20 and month == "março":
    print("Você é do signo de peixes")
