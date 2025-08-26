class Vendas():
    def __init__(self,nome):
        self.nome = nome
        self.vendas = 0 
    def vendeu(self,vendas):
        self.vendas = vendas
    def bateu_meta(self,meta):
        if self.vendas >= meta:
            print(f'{self.nome} Bateu a meta!')
        else:
            print(f'{self.nome} Não bateu a meta!')

vendedor1 = Vendas('Geronimo Antonio')
vendedor1.vendeu(500)
vendedor1.bateu_meta(600)

vencedor2 = Vendas('Claudinei Ramos')
vencedor2.vendeu(1000)
vencedor2.bateu_meta(500)