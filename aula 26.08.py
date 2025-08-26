
class Carro:

    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir(self):
        print(f'{self.marca}:{self.modelo}:{self.ano}')

carro1 = Carro('Toyota','Corolla', 2020)
carro1.exibir()
carro2 = Carro('Wolkswagem','Gol',2010)
carro2.exibir()
carro3 = Carro('Ferrari','GT450',2022)
carro3.exibir()