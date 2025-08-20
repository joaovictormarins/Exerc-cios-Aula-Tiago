#4 jogadores jogam o dado e resultem números aleatórios

from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogos = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado' )
    sleep(1)
print('-='*30)

ranking = sorted(jogos.items(),key=itemgetter(1),revrse=True)
print('=============== Ranking dos jogadores ===================')
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar:{v[0]} com {v[1]} pontos')
    sleep(1)
print('-='*30)


