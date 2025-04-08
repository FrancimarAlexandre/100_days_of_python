# EXEMPLO

lista = ['casa','escola','python']
for i in lista:
    print(i)

# LOOPING ATRVÉS DE UMA CADEIA DE CARACTERES
for i in "python":
    print(i)

# BREAK

# sair do loop quando estiver "escola"
lista = ['casa','escola','python']
for i in lista:
    print(i)
    if i == 'escola':
        break

# sair do loop quando estiver "escola", mas agora quebra antes da impressão
lista = ['casa','escola','python']
for i in lista:
    if i == 'escola':
        break
    print(i)
