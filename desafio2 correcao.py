class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    def depositar(self,valor):
        self.saldo += valor
        print('Saldo:', self.saldo)

c1 = Conta('Maria')
c1.depositar(200)
