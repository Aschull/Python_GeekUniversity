"""
 Documentando funções com Docstrings
 Para acessar a documentaão podemos utilizar __doc__ ou help()
"""


def diz_oi():
    """
    Função simples para retornar uma string 'Oi'
    :return: 'Oi'
    """
    return 'Oi'


def exponecial(num, expoente=2):
    """
    FUnção q eleva a variavel num ao quadrado
    :param num: número a ser elevado
    :param expoente: expoente padrão 2, poderá ser informado outro valor para expoente.
    :return: num elevado ao expoente
    """
    return num ** expoente


