#Exercício jogador da mega-sena criar palpites

import time 
from random import randint 

lista = []
jogos = []
contador = 0 
print('-='*8, 'Jogo da Mega-Sena', '-='*8)

quantidade = (int(input('Quantos jogos  você deseja fazer? \nR: ')))
total = 1
while total <= quantidade:
    cont = 0 
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont+= 1 
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1 

(print('-='*6, f'sorteando {quantidade} jogos','-='*6))
for i, n in enumerate (jogos):
    time.sleep(1)
    print(f'{i+1}° jogo: {n}')
time.sleep(1)
print('-='*6,'Boa Sorte!', '-='*6)