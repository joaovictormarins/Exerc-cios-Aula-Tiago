class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        print(f'Olá, sou {self.nome}: tenho {self.idade} anos')

pessoa1 = Pessoa('Victor' , 18)
pessoa1.exibir()
pessoa2 = Pessoa('Clodoaldo' , 55)
pessoa2.exibir() 