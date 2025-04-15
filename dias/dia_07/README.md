# 📅 Dia 7 —  Strings e manipulação de texto

**String** uma sequência de caracteres usado para representar um texto. Em Python, uma string pode ser definida utilizando aspas simples **('texto')**, aspas duplas **("texto")** ou até mesmo aspas triplas **('''texto''' ou """texto""")**. Cada uma dessas formas tem seu propósito:

```python
# Diferentes formas de definir strings
string1 = 'Olá, mundo!'    # Aspas simples
string2 = "Olá, mundo!"    # Aspas duplas
string3 = '''Olá, mundo!'''  # Aspas triplas
string4 = """Olá, mundo!"""  # Aspas triplas

print(string1)
print(string2)
print(string3)
print(string4)
```

As aspas triplas são especialmente úteis para definir strings de múltiplas linhas:

```python
texto_multilinhas = """Isso é um exemplo de
uma string que ocupa
múltiplas linhas."""
print(texto_multilinhas)
```

Strings em Python são **imutáveis**, uma vez criadas, não podem ser modificadas diretamente. Se precisar alterar uma string, é necessário criar uma nova variável.

# CRIANDO E MANIPULANDO STRING EM PYTHON 

Python oferece diversas maneiras de **manipular strings**, incluindo operações básicas como acesso a caracteres, fatiamento e repetição.

- Acessando caracteres em uma string

    Cada caractere dentro de uma string pode ser acessado utilizando indexação. Em Python, os índices começam em 0.

````python
texto = "Python"
print(texto[0])  # Saída: P
print(texto[3])  # Saída: h
````

Também é possível utilizar índices negativos para acessar os caracteres do final para o início.

````python
print(texto[-1])  # Saída: n (último caractere)
print(texto[-3])  # Saída: h
````

- Fatiamento de strings

    O fatiamento (slicing) permite extrair partes específicas de uma string. A sintaxe é:
    ```` python
    string[início:fim:passo]

exemplo

````python
texto = "Python"print(texto[0:4])   # Saída: Pyth
print(texto[:4])    # Saída: Pyth (início implícito)
print(texto[2:])    # Saída: thon (fim implícito)
print(texto[::2])   # Saída: Pto (passo de 2 em 2)
print(texto[::-1])  # Saída: nohtyP (string invertida)
````
- Repetição e concatenação

    Strings podem ser repetidas e concatenadas facilmente:

    ````python
    print("Py" + "thon")   # Saída: Python (concatenação)<br>print("A" * 5)        # Saída: AAAAA (repetição)<br>
    ````

PRINCPAIS MÉTODOS PARA TRABALHAR COM STRINGS

Python oferece diversos métodos embutidos para manipulação de strings. Esses métodos facilitam tarefas como alteração de caixa, substituição de caracteres, remoção de espaços, e muito mais.

- Convertendo caixa de texto

    Python permite converter todas as letras de uma string para maiúsculas, minúsculas ou capitalizar a primeira letra:

    ````python
    texto = "python é incrível"
    print(texto.upper()) # PYTHON É INCRÍVEL
    print(texto.lower())      # python é incrível
    print(texto.title())      # Python É Incrível
    print(texto.capitalize()) # Python é incrível

    - upper(): Converte toda a string para maiúsculas.
    - lower(): Converte toda a string para minúsculas.
    - title(): Converte a primeira letra de cada palavra para maiúscula.
    - capitalize(): Apenas a primeira letra da string fica maiúscula.

# Removendo espaços em branco
````python
texto = "   Python   "

print(texto.strip())   # "Python" (remove espaços nas extremidades)
print(texto.lstrip())  # "Python   " (remove espaços à esquerda)
print(texto.rstrip())  # "   Python" (remove espaços à direita)
````
- strip(): Remove espaços em branco no início e no fim.
- lstrip(): Remove apenas os espaços da esquerda.
- rstrip(): Remove apenas os espaços da direita.

# Substituição de caracteres
````python
frase = "Eu gosto de Java"
nova_frase = frase.replace("Java", "Python")
print(nova_frase)  # Saída: Eu gosto de Python
````
# Dividindo e unindo strings
````python
frase = "Aprender Python é divertido"
palavras = frase.split()  # Divide a string em uma lista de palavras
print(palavras)  # ['Aprender', 'Python', 'é', 'divertido']

# Agora unimos as palavras novamente com um hífen
nova_frase = "-".join(palavras)
print(nova_frase)  # Aprender-Python-é-divertido
````
- split(): Divide a string em uma lista, separando pelos espaços (ou outro delimitador definido).
- join(): Junta elementos de uma lista em uma única string, com um delimitador.

# Verificando o conteúdo de uma string
````python
texto = "Python é incrível"

print(texto.startswith("Python"))   # True
print(texto.endswith("incrível"))   # True
print("Python" in texto)            # True (verifica se a palavra está presente)
print("Java" not in texto)          # True (verifica se a palavra não está presente)
````
# Concatenação e formatação de strings

# Concatenação de strings
````python
nome = "Python"
versao = "3.10"
frase = nome + " versão " + versao
print(frase)  # Saída: Python versão 3.10

# f-strings
frase = f"{nome} versão {versao}"
print(frase)  # Saída: Python versão 3.10
````
# Formatando strings

# 1. f-strings (Python 3.6+)
````python
nome = "Alice"
idade = 25
mensagem = f"Meu nome é {nome} e tenho {idade} anos."
print(mensagem)  # Saída: Meu nome é Alice e tenho 25 anos.

# Também é possível realizar operações dentro das f-strings:
a = 5
b = 3
print(f"A soma de {a} + {b} é {a + b}")  # Saída: A soma de 5 + 3 é 8
````
# 2. Método .format()
````python
mensagem = "Meu nome é {} e tenho {} anos.".format("Alice", 25)
print(mensagem)  # Saída: Meu nome é Alice e tenho 25 anos.

mensagem = "Meu nome é {0} e tenho {1} anos.".format("Alice", 25)
print(mensagem)  # Saída: Meu nome é Alice e tenho 25 anos.

mensagem = "Meu nome é {nome} e tenho {idade} anos.".format(nome="Alice", idade=25)
print(mensagem)  # Saída: Meu nome é Alice e tenho 25 anos.
````
# 3. Formatação com % (método antigo)
````python
nome = "Alice"
idade = 25
mensagem = "Meu nome é %s e tenho %d anos." % (nome, idade)
print(mensagem)  # Saída: Meu nome é Alice e tenho 25 anos.
````
# Formatando números em strings
````python
pi = 3.14159
print(f"Valor de pi: {pi:.2f}")  # Saída: Valor de pi: 3.14
````
# Strings em Python e expressões regulares
````python
import re

# Buscando padrões em strings
texto = "Meu número de telefone é 1234-5678"
padrao = r"\d{4}-\d{4}"
resultado = re.search(padrao, texto)

if resultado:
    print(f"Encontrado: {resultado.group()}")  # Saída: Encontrado: 1234-5678
````
# Encontrando múltiplos padrões
````python
texto = "Contate-me nos telefones 1234-5678 ou 9876-5432"
padrao = r"\d{4}-\d{4}"
resultados = re.findall(padrao, texto)
print(resultados)  # Saída: ['1234-5678', '9876-5432']
````
# Substituindo padrões em strings
````python
texto = "Meu número é 1234-5678"
novo_texto = re.sub(r"\d{4}-\d{4}", "XXXX-XXXX", texto)
print(novo_texto)  # Saída: Meu número é XXXX-XXXX
````
# Verificando se uma string segue um padrão
````python
email = "usuario@email.com"
padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.fullmatch(padrao, email):
    print("Email válido!")
else:
    print("Email inválido!")
````
# Exemplo prático: extração de URLs
````python
texto = "Visite nosso site em https://www.exemplo.com e https://outrosite.com"
padrao = r"https?://[a-zA-Z0-9./-]+"
urls = re.findall(padrao, texto)
print(urls)  # Saída: ['https://www.exemplo.com', 'https://outrosite.com']
````

