# 📅 Dia 5 —  Listas, Tuplas e Compreensões em Python

Python oferece diversas estruturas para armazenar coleções de dados. As mais comuns são **listas**, **tuplas** e as **compreensões de listas** (list comprehensions).

---

## 📋 Listas (`list`)

Uma lista é **mutável**, **ordenada** e **permite valores duplicados**.

### 🔧 Criando uma lista

```python
fruits = ["apple", "banana", "cherry"]
```

### 📌 Acessando elementos

```python
print(fruits[0])     # apple
print(fruits[-1])    # cherry
```

### ✏️ Modificando elementos

```python
fruits[1] = "blueberry"
```

### ➕ Adicionando elementos

```python
fruits.append("orange")        # adiciona ao final
fruits.insert(1, "kiwi")       # insere na posição 1
```

### ➖ Removendo elementos

```python
fruits.remove("apple")         # remove por valor
fruits.pop()                   # remove o último
del fruits[0]                  # remove por índice
```

### 🔄 Iterando sobre listas

```python
for fruit in fruits:
    print(fruit)
```

---

## 📦 Tuplas (`tuple`)

Uma tupla é **imutável**, **ordenada** e **permite valores duplicados**.

### 🔧 Criando uma tupla

```python
dimensions = (20, 40, 80)
```

### 📌 Acessando elementos

```python
print(dimensions[0])  # 20
```

### ❌ Modificando elementos

```python
# Não é possível modificar diretamente
# dimensions[0] = 10  # Isso geraria um erro
```

---

## ⚡ Compreensões de Lista (List Comprehension)

Forma concisa e elegante de criar listas.

### 🔄 Criar uma lista com base em outra

```python
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
# Resultado: [1, 4, 9, 16, 25]
```

### 🔎 Com condição (filter)

```python
even = [n for n in numbers if n % 2 == 0]
# Resultado: [2, 4]
```

### 🧠 Com expressão mais complexa

```python
labels = [f"Item {n}" for n in range(1, 4)]
# Resultado: ['Item 1', 'Item 2', 'Item 3']
```

---

## 📚 Referências

- [Documentação Oficial – Tipos de sequência](https://docs.python.org/pt-br/3/library/stdtypes.html#sequence-types-list-tuple-range)
- *Python Fluente* – Luciano Ramalho
