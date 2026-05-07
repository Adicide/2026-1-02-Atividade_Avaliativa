# 3. Escreva um programa que recebe um inteiro positivo numero e determina se numero é um número perfeito 
# (um número é perfeito se a soma de seus divisores próprios é igual a ele mesmo, ex: 6 = 1+2+3).

numero = int(input('Digite um número: '))

soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print(f'\n{numero} é Perfeito.')
else:
    print(f'\n{numero} Não é perfeito.')