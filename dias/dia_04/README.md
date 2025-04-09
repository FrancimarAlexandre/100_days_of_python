## 📅 Dia 4 — Laços (`for`, `while`) e controle de fluxo

Em Python, o laço `for` é usado para iterar sobre objetos iteráveis como listas, tuplas, strings, dicionários e conjuntos.

---

## 🔁 Sintaxe Básica

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

- Não é necessário declarar um índice manualmente.
- Funciona diretamente sobre itens iteráveis.

---

## 🔡 Iterando sobre Strings

Strings também são iteráveis:

```python
for letter in "banana":
    print(letter)
```

---

## ⛔️ `break`: Interrompe o loop

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
```

---

## 🔁 `continue`: Pula para a próxima iteração

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
```

---

## 🔢 `range()`: Iterações com números

```python
# De 0 a 5
for i in range(6):
    print(i)

# De 2 a 5
for i in range(2, 6):
    print(i)

# De 2 a 29, pulando de 3 em 3
for i in range(2, 30, 3):
    print(i)
```

---

## 🧾 `else` com `for`

Executado quando o loop termina normalmente (sem `break`):

```python
for i in range(6):
    print(i)
else:
    print("Finalizado com sucesso!")
```

> **Nota:** o bloco `else` **não** será executado se o loop for interrompido com `break`.

---

## 🔁 Loops Aninhados

Um loop dentro de outro:

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for f in fruits:
        print(a, f)
```

---

## ⛳️ `pass`: Usado para criar um bloco vazio

```python
for x in [0, 1, 2]:
    pass  # Evita erro de sintaxe se o bloco estiver vazio
```

---

## 📚 Referências

- [w3schools](https://www.w3schools.com/python/python_for_loops.asp)
- *Python Fluente* – Luciano Ramalho
