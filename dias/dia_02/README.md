## 📅 Dia 2 — Sintaxe básica, tipos primitivos e variáveis

`Sintaxe`

A sintaxe do Python é projetada para ser clara e legível. Diferente de muitas linguagens, ela usa indentação (espaços ou tabulação) para definir blocos de código:

    if True:
        print("Isso está dentro do bloco")
    print("Isso está fora do bloco")

### Outros pontos importantes:

- Comentários: Começam com #

- Fim de linha: Python não usa ;

- Case-sensitive: variavel e Variavel são diferentes,
Case-sensitive significa que letras maiúsculas e minúsculas são tratadas como diferentes. Isso se aplica a nomes de variáveis, funções, classes, etc.

---
    nome = "João"
    Nome = "Maria"
    print(nome)  # João
    print(Nome)  # Maria


`Tipos primitivos e variáveis`

Tipos primitivos são os tipos de dados básicos que uma linguagem de programação oferece de forma nativa. Eles são os blocos fundamentais para armazenar e manipular valores simples.

### Em Python, os principais tipos primitivos são:

|Tipo|Exemplo	|Descrição                             |
|----|----------|--------------------------------------|
|int|10, -3, 0|Números inteiros (sem casas decimais)|
|float|	3.14, -0.5, 0.0|Números com ponto flutuante (decimais)|
|bool|True, False	|Valores booleanos (verdadeiro ou falso)|
|str|"Olá", 'Python'|Cadeia de caracteres (texto)|

### Exemplos de uso

    idade = 25           # int
    altura = 1.75        # float
    nome = "Ana"         # str
    estudando = True     # bool

Python faz inferência de tipo, ou seja, você não precisa declarar o tipo explicitamente.

### Você pode verificar o tipo com type()

    print(type(idade))     # <class 'int'>
    print(type(altura))    # <class 'float'>
    print(type(nome))      # <class 'str'>
    print(type(estudando)) # <class 'bool'>


`Variáveis`

Variáveis armazenam valores. Em Python, você não precisa declarar o tipo:

    nome = "Alice"         # string
    idade = 25             # int
    altura = 1.68          # float
    ativo = True           # bool

- Python usa tipagem dinâmica

- Pode alterar o tipo da variável ao longo do código

- Nomes de variáveis devem começar com letra ou _, e não podem conter espaços ou caracteres especiais

### Boas práticas:

- Use nomes significativos (contador, nome_usuario)

- Siga o padrão snake_case

### Tipagem dinâmica

Tipagem dinâmica é uma característica de determinadas linguagens de programação que não exigem declarações de tipos de dados. 

### snake_case

snake_case é um estilo de escrita muito usado em programação, onde palavras são separadas por underscores (_) e todas as letras são minúsculas.

#### Onde usar snake_case em Python?

O snake_case é a convenção oficial do Python (conforme a PEP 8) para:

    Nomes de variáveis

    Nomes de funções

    Parâmetros

    Arquivos e módulos