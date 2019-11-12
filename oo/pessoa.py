class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luiz = Pessoa(nome='Luiz')
    gustavo = Pessoa(luiz, nome='Gustavo')
    print(Pessoa.cumprimentar(gustavo))
    print(id(gustavo))
    print(gustavo.cumprimentar())
    print(gustavo.nome)
    print(gustavo.idade)
    for filho in gustavo.filhos:
        print(filho.nome)
    gustavo.sobrenome = 'Mendes'
    del gustavo.filhos
    print(gustavo.__dict__)
    print(luiz.__dict__)