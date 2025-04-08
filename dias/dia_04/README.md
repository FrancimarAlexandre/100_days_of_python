## 📅 Dia 4 — Laços (`for`, `while`,`match`) e controle de fluxo

`for`

usado oara iterar em uma sequência(lista,tupla,dicionário)

EXEMPLO

[código](scripts/for.py)

LOOPING ATRAVÉS DE UMA CADEIA DE CARACTERES

mesmo as strings são objetos iteráveis, elas contêm uma sequência de caracte

[código](scripts/for.py)

BRAEK

podemos parar antes de percorrer todos os itens

[código](scripts/for.py)

CONTINUE

[código](scripts/for.py)

RANGE

Para percorrer um conjunto de códigos um número especificado de vezes, podemos usar a função range(),
A função range() retorna uma sequência de números, começando em 0 por padrão, e incrementa em 1 (por padrão) e termina em um número especificado.

A função range() é padronizada para 0 como um valor inicial, no entanto, é possível especificar o valor inicial adicionando um parâmetro: range(2, 6), que valores médios de 2 a 6 (mas não incluindo 6):

[código](scripts/for.py)



`while`

Com o loop `while` podemos executar um conjunto de instruções, desde que uma condição seja verdadeira.

SINTAXE

    while condição:
        code block

[código](scripts/while.py)

`OBS`-> Lembre-se de incrementar i, ou então o loop continuará para sempre.

BREAK

podemos para o loop mesmo que a condição ainda seja válida.

[código](scripts/while.py)

CONTINUE

podemos para a iteração atual e continue com a proxima.

[código](scripts/while.py)

ELSE

podemos executar um bloco uma vez quando a condição não é mais válida.

[código](scripts/while.py)

`match`

Em vez de escrever muitas instruções, você pode usar a instrução `match`

SINTAXE

    match expresion:
    case x:
        code block
    case y:
        code block
    case z:
        code block

[código](scripts/match.py)

- A expreção é avaliada uma vez e compara com os valores de cada `case`.

VALOR PADRÃO

use o caractere underscores `_` como último case, ele vai exercutar quando não houver outras correspondências.

[código](scripts/match.py)

COMBINAR VALORES

use o caractere de barra vertical `|` como um operador para verificar mais de uma correspondência.

[código](scripts/match.py)

INSTRUÇÕES `IF` COMO GUARDS

podemos adicionar instruções na avaliação de caso como uma verificação de condição extra.

[código](scripts/match.py)
