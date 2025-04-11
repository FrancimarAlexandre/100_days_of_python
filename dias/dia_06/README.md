# 📅 Dia 6 —  Dicionários e Conjuntos em Python

Python oferece duas estruturas poderosas para agrupar e gerenciar dados: **dicionários** e **conjuntos**. Ambos são úteis para organizar informações de forma eficiente.

---

## 📖 Dicionários (`dict`)

Um dicionário é uma coleção **desordenada**, **mutável** e **indexada por chaves únicas**.

### 🔧 Criando um dicionário

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "São Paulo"
}
```

### 📌 Acessando e modificando valores

```python
print(person["name"])     # Alice
person["age"] = 31        # atualiza valor
```

### ➕ Adicionando novas chaves

```python
person["email"] = "alice@email.com"
```

### ➖ Removendo chaves

```python
person.pop("city")        # remove "city"
del person["age"]         # remove "age"
```

### 🔁 Iterando sobre um dicionário

```python
for key, value in person.items():
    print(key, ":", value)
```

### 🧰 Métodos úteis

```python
person.keys()      # retorna todas as chaves
person.values()    # retorna todos os valores
person.items()     # retorna pares (chave, valor)
```

---

## 🧮 Conjuntos (`set`)

Um conjunto é uma coleção **desordenada**, **imutável (quanto aos elementos)** e **sem itens duplicados**.

### 🔧 Criando um conjunto

```python
fruits = {"apple", "banana", "cherry"}
```

### ➕ Adicionando elementos

```python
fruits.add("orange")
```

### ➖ Removendo elementos

```python
fruits.remove("banana")   # erro se não existir
fruits.discard("banana")  # não dá erro se não existir
```

### 🔁 Iterando sobre conjuntos

```python
for fruit in fruits:
    print(fruit)
```

### 📊 Operações entre conjuntos

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)         # {1, 2, 3, 4, 5}
a.intersection(b)  # {3}
a.difference(b)    # {1, 2}
```

> 🔎 Dica: Sets são ótimos para eliminar duplicatas de uma lista!

```python
lista = [1, 2, 2, 3, 3, 3]
unicos = set(lista)  # {1, 2, 3}
```

---

## 📚 Referências

- [Documentação Oficial – dicionários](https://docs.python.org/pt-br/3/library/stdtypes.html#mapping-types-dict)  
- [Documentação Oficial – conjuntos](https://docs.python.org/pt-br/3/library/stdtypes.html#set-types-set-frozenset)  
- *Python Fluente* – Luciano Ramalho
