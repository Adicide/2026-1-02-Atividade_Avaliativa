# 1. Escreva um programa Python que exiba na tela uma sequência de 10 números inteiros aleatórios entre 1 e 100.

import random

for i in range(10):
    num = random.randint(1, 100)
    print(num)