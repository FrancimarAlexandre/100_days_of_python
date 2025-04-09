## 📅 Dia 4 — Laços (`for`, `while`) e controle de fluxo


Em Python, os laços `for` e `while` são usados para repetir blocos de código diversas vezes, com base em coleções de dados (`for`) ou em uma condição (`while`).

---

## 🔁 Laço `for`

O `for` é usado para iterar sobre objetos iteráveis como listas, tuplas, strings, dicionários e conjuntos.

### ✅ Sintaxe Básica

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 🔡 Iterando sobre Strings

```python
for letter in "banana":
    print(letter)
```

### ⛔️ `break`: Interrompe o loop

```python
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
```

### 🔁 `continue`: Pula para a próxima iteração

```python
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
```

### 🔢 `range()`: Iterações com números

```python
for i in range(6):          # 0 a 5
    print(i)

for i in range(2, 6):       # 2 a 5
    print(i)

for i in range(2, 30, 3):   # 2 a 29, pulando de 3 em 3
    print(i)
```

### 🧾 `else` com `for`

```python
for i in range(6):
    print(i)
else:
    print("Finalizado com sucesso!")
```

> ⚠️ O bloco `else` **não será executado** se o loop for interrompido com `break`.

### 🔁 Loops Aninhados

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for f in fruits:
        print(a, f)
```

### ⛳️ `pass`: Bloco vazio

```python
for x in [0, 1, 2]:
    pass
```

---

## 🔁 Laço `while`

O `while` executa um bloco de código **enquanto uma condição for verdadeira**.

### ✅ Sintaxe Básica

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

### ⛔️ `break` com `while`

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

### 🔁 `continue` com `while`

```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

### 🧾 `else` com `while`

```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Laço finalizado com sucesso!")
```

> ⚠️ O bloco `else` também é ignorado se houver um `break`.

---

## 📚 Referências

- [Documentação Oficial do Python – for loops](https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements)
- [Documentação Oficial do Python – while loops](https://docs.python.org/pt-br/3/tutorial/introduction.html#first-steps-towards-programming)
- *Python Fluente* – Luciano Ramalho
