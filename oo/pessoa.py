class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    gustavo.olhos = 1
    del gustavo.olhos
    print(gustavo.__dict__)
    print(luiz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(gustavo.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(gustavo.olhos), id(luiz.olhos))
    print(Pessoa.metodo_estatico(), gustavo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), gustavo.nome_e_atributos_de_classe())