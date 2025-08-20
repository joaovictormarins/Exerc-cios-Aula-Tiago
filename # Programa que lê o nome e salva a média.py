# Programa que lê o nome e salva a média do aluno
#com base na média ele terá as situações: Aprovado,Reprovado, Em Recuperação
# Acima de 7: Aprovado
# Abaixo de 4 e 6.9: Em Recuperação
# abaixo de 4: Reprovado

aluno = []
situacao = {} #serve o dicionário


for i in range (0,2):
    situacao['nome'] = input('Digite seu nome:  ')
    situacao['nota'] = float(input('Digite sua nota:  '))

    aluno.append(situacao.copy())
   
    if situacao['nota']>= 7:
        print('Você foi Aprovado')
    elif  4 <= situacao['nota'] < 7:
        print('Você está em recuperação')
    else:
        print('Você está reprovado')   




