# 🐍 Python Week11 Lesson

# 📌 Tuple

A **tuple** is a collection of values.

### Features

- ✅ Ordered
- ✅ Immutable (cannot be changed after creation)
- ✅ Allows duplicate values

> Use a tuple when your data should be **read-only** and should not be modified accidentally.

## Creating Tuples

```python
# Single-value tuple
tup1 = (50,)

# Multiple-value tuple
tup2 = ("Alix", 23, "August")
```

> **Note:** A single-value tuple **must** have a comma.

```python
tup = (50,)   # ✅ Tuple
tup = (50)    # ❌ Integer
```

---

## Accessing Tuple Values

```python
tup3 = (1, 2, 3, 4, 5)

print(tup3[0])     # 1
print(tup3[-1])    # 5
print(tup3[1:3])   # (2, 3)
```

### Indexing

| Code | Output |
|------|--------|
| `tup3[0]` | `1` |
| `tup3[-1]` | `5` |
| `tup3[1:3]` | `(2, 3)` |

---

## Tuple Methods

```python
letters = ('a', 'b', 'a', 'b')
```

### `.index()`

Returns the first position of a value.

```python
letters.index('a')
# Output: 0
```

```python
letters.index('c')
# ValueError
```

---

### `.count()`

Counts how many times a value appears.

```python
letters.count('a')
# Output: 2

letters.count('c')
# Output: 0
```

---

# 📌 Dictionary

A **dictionary** stores data as **key-value pairs**.

## Features

- ✅ Mutable
- ✅ Stores data as key-value pairs
- ✅ Keys must be unique
- ❌ Cannot access items using indexes

---

## Creating a Dictionary

```python
dict1 = {
    "name": "August",
    "age": 23,
    "country": "Japan"
}
```

---

## Accessing Values

```python
print(dict1["name"])
print(dict1["age"])
print(dict1["country"])
```

Output

```
August
23
Japan
```

If the key doesn't exist:

```python
print(dict1["city"])
```

```
KeyError
```

---

## `.get()`

Safely gets a value.

```python
print(dict1.get("name"))
# August

print(dict1.get("city"))
# None
```

Unlike `[]`, `.get()` **does not** raise an error if the key doesn't exist.

---

## Add or Replace Items

### Replace

```python
dict1["name"] = "Alix"
```

### Add

```python
dict1["major"] = "Fine Art"
```

Result

```python
{
    "name": "Alix",
    "age": 23,
    "country": "Japan",
    "major": "Fine Art"
}
```

---

## `.pop()`

Removes a key and returns its value.

```python
dict1.pop("major")
```

Output

```
Fine Art
```

Using a default value:

```python
name = dict1.pop("name", None)
city = dict1.pop("city", None)

print(name)
print(city)
```

Output

```
Alix
None
```

---

# Looping Through a Dictionary

```python
character = {
    "name": "August",
    "age": "20",
    "country": "Japan"
}
```

---

## Get Keys

```python
for key in character:
    print(key)
```

Output

```
name
age
country
```

---

## Get Values

```python
for value in character.values():
    print(value)
```

Output

```
August
20
Japan
```

---

## Get Values Using Keys

```python
for key in character:
    print(character[key])
```

Output

```
August
20
Japan
```

---

## Check if a Key Exists

```python
print("name" in character)
# True

print("city" not in character)
# True
```

---

## `len()`

Returns the number of key-value pairs.

```python
print(len(character))
```

Output

```
3
```

---

## `.update()`

Adds new items or replaces existing ones.

```python
d1 = {
    "apple": 1.1,
    "banana": 1.2,
    "kiwi": 1.3
}

d2 = {
    "cake": 2.1,
    "coffee": 2.2,
    "bread": 2.3
}

d1.update(d2)
```

Result

```python
{
    'apple': 1.1,
    'banana': 1.2,
    'kiwi': 1.3,
    'cake': 2.1,
    'coffee': 2.2,
    'bread': 2.3
}
```

---

## `.copy()`

Creates a copy of the dictionary.

```python
d3 = d1.copy()
```

---

## `.keys()`

Returns all keys.

```python
print(d1.keys())
```

---

## `.values()`

Returns all values.

```python
print(d1.values())
```

---

## `.items()`

Returns all key-value pairs.

```python
print(d2.items())
```

Output

```python
dict_items([
    ('cake', 2.1),
    ('coffee', 2.2),
    ('bread', 2.3)
])
```

---

## `.clear()`

Removes every item.

```python
d3.clear()
```

Output

```python
{}
```

> **Note:** `clear()` empties the dictionary. If you do `print(d3.clear())`, it prints `None` because `clear()` doesn't return anything.

---

# 📌 Object-Oriented Programming (OOP)

OOP is a way of organizing code using **classes** and **objects**.

Example:

| Concept | Example |
|----------|----------|
| Class | Dog |
| Objects | Dog1, Dog2 |
| Attributes | name, age, color |
| Methods | bark(), run(), eat() |

---

# Creating a Class

```python
class Animal:

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
```

### Create Objects

```python
a1 = Animal("Rex", "Dog", "Woof")
a2 = Animal("Whiskers", "Cat", "Meow")
```

### Access Attributes

```python
print(a1.name)
print(a1.sound)

print(a2.name)
print(a2.sound)
```

Output

```
Rex
Woof
Whiskers
Meow
```

---

# Methods

Methods are functions inside a class.

```python
class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"
```

```python
a1 = Animal("Rex", "Woof")

print(a1.speak())
```

Output

```
Rex says Woof
```

---

# `__str__()`

`__str__()` controls what is displayed when you print an object.

```python
class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.name} from {self.course}"
```

```python
s1 = Student("Alix", "Immersive Media")
s2 = Student("August", "Fine Art")

print(s1)
print(s2)
```

Output

```
Alix from Immersive Media
August from Fine Art
```

---

# Constructor + Method + `__str__()`

```python
class Animal:

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"{self.name} the {self.species}"
```

```python
a1 = Animal("Rex", "Dog", "Woof")

print(a1.speak())
print(a1)
```

Output

```
Rex says Woof
Rex the Dog
```

---

# ⭐ Summary

## Tuple

- Ordered
- Immutable
- Allows duplicates
- Access using indexes
- Useful for read-only data

---

## Dictionary

- Stores key-value pairs
- Mutable
- Keys are unique
- Fast lookup using keys
- Common methods:
  - `get()`
  - `pop()`
  - `update()`
  - `copy()`
  - `keys()`
  - `values()`
  - `items()`
  - `clear()`

---

## OOP

- **Class** → Blueprint
- **Object** → Instance of a class
- **Attribute** → Variable inside an object
- **Method** → Function inside a class
- `__init__()` → Constructor
- `__str__()` → Controls how objects are printed
