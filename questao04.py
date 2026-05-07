# 4. Escreva um programa que leia um inteiro positivo numero e exibe o número de dígitos de numero.

numero = int(input('Digite um número: '))
numero_str = str(numero)
digitos_numero = len(numero_str)

print(f'\nQuantidade de dígitos de {numero}: {digitos_numero}')