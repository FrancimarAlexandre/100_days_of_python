# MATCH

n = 2

match n:
    case 1:
        print("Hello World")
    case 2:
        print('olá mundo')
    case 3:
        print('100 days of python')

# VALOR PADRÃO

m = 4

match m:
    case 1:
        print("Hello World")
    case 2:
        print('olá mundo')
    case 3:
        print('100 days of python')
    case _:
        print('valor incorreto')

# COMBINAR VALORES

o = 5

match o:
    case 1|3|5:
        print("o valor é Ímpar")
    case 2|4|6:
        print('o valor é Par')

# INSTRUÇÃO IF COMO GUARDS

mes = 5
dia = 4

match dia:
    case 1|2|3|4|5 if mes == 4:
        print('Um dia da semana em Abril')
    case 1|2|3|4|5 if mes == 5:
        print('Um dia da semana em Maio')
    case _:
        print("mês invalido")