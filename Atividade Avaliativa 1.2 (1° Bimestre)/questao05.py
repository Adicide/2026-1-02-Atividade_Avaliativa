# 5. Escreva um programa que leia um número inteiro positivo repeticoes, depois leia repeticoes números inteiros e calcule:
# a soma total,
# a média,
# o maior valor,
# o menor valor,
# a quantidade de valores acima da média.

repeticoes = int(input('Digite a quantidade de repetições: '))
print('')

soma = 0
listanums = []
acima_media = 0
media = 0
valor = 1
for i in range(repeticoes):
    num = int(input(f'Insira o valor {valor}: '))
    soma += num
    listanums.append(num)
    valor += 1

media = soma / repeticoes
for a in listanums:
    if a > media:
        acima_media += 1

maior = max(listanums)
menor = min(listanums)

print(f'\nSoma total: {soma}')
print(f'Média: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Quantidade de valores acima da média: {acima_media}')