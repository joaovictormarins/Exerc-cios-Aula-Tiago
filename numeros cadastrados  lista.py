numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'valor {n} já existe na lista...')
    resposta = input('Quer continuar? [S/N] ')
    if resposta in 'Nn':
        break 
print('-='*30)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
numeros.sort(reverse=True)
print(f'Os valores em ordem crescente são: {numeros}')
