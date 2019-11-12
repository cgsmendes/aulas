def contar(s):
    """

    Função que conta os caracteres de uma string

    Ex:
    >>> contar('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    >>> contar('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    :return: retorna um print na tela

    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar('renzo'))
    print()
    print(contar('banana'))