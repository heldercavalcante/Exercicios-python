"""
Calculando o IMC
"""
nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
ano_atual = 2022
ano_nascimento = int(input('Digite o ano em que nasceu: '))
imc = peso/(altura**2)
print(f'\n{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg \nO imc  de {nome} é {imc:.2f}. \n{nome} nasceu em {ano_nascimento}.')



