numeros = []
pares = []
impares = []


while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N]: ')
    if resp in'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'a lista completa é: {numeros}')
print(f'a lista de pares é: {pares}')
print(f'a lista de ímpares é: {impares}')


