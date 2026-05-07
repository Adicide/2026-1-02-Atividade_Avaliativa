# 2. Escreva um programa Python que leia um número inteiro positivo e armazene na variável repeticoes; 
# e exiba na tela uma sequência de repeticoes números inteiros aleatórios entre 1 e 100

import random

n = int(input('Quantos números aleatórios você quer? > '))
print('')
repeticoes = n

for i in range(0, repeticoes):
    num = random.randint(1, 100)
    print(num)