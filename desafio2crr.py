class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    def depositar(self, valor):
        self.saldo = valor 
        print(f'Saldo da conta:{self.saldo}')

conta1 = Conta('Maria Neves')
conta1.depositar(int(input(f'{conta1.titular} Quanto você deseja depositar? ')))