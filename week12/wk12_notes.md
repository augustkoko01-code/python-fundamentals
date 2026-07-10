# Python OOP Study Notes

## Class Modelling

**Class modelling** is the process of identifying **classes**, **attributes**, and **methods** from a problem description before coding.

- **Attributes** → Characteristics or properties of a class.
- **Methods** → Actions or behaviors that a class can perform. Methods are functions defined inside a class.
- Decide what classes you need from the problem description.
- **Nouns** → Usually become **classes** or **attributes**.
- **Verbs** → Usually become **methods**.

---

# Example 1: Exhibit Class

```python
class Exhibit:
    def __init__(self, name, price, visitors, capacity):
        self.name = name        # 'Reptiles'
        self.price = price      # 5
        self.visitors = visitors    # 120
        self.capacity = capacity    # 400

    def revenue(self):
        return self.price * self.visitors
        # 5 * 120 = 600
        # 8 * 540 = 4320

    def occupancy_rate(self):
        return round(self.visitors / self.capacity * 100, 1)
        # (120 / 400) * 100 = 30.0
        # (540 / 600) * 100 = 90.0

    # A method can call another method on the same object
    def status():
        rate = self.occupancy_rate()
        # rate = 30.0
        # rate = 90.0

        if rate >= 90:
            return 'Packed'
        elif rate >= 60:
            return 'Busy'
        else:
            return 'Quiet'

    def summary(self):
        return f'{self.name}: ${self.revenue()}\n{self.occupancy_rate()}% {self.status()}'
```

### Store multiple objects in a list

```python
exhibits = [
    Exhibit('Reptiles', 5, 120, 400),
    Exhibit('Lions', 8, 540, 600),
    Exhibit('Penguins', 6, 380, 400)
]
```

### Loop through every object

```python
for e in exhibits:
    print(e.summary())
```

### Output

```text
Reptiles: $600
30.0% Quiet
Lions: $4320
90.0% Packed
Penguins: $2280
95.0% Packed
```

---

# Best Object (Best-So-Far Algorithm)

Assume the **first object** is the best.

```python
best = exhibits[0]
```

Loop through every object and compare it with the current best.

```python
for e in exhibits:
    if e.revenue() > best.revenue():
        best = e

print('Top earner:', best.name)
```

### Output

```text
Top earner: Lions
```

---

# Inheritance

A **subclass** inherits the **attributes** and **methods** from its **parent class**.

## Parent Class

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def summary(self):
        return f'{self.name}'
```

---

## First Subclass - Dog

```python
class Dog(Animal):
    # Dog inherits attributes and methods from Animal

    def __init__(self, name):
        # super() reuses the parent constructor
        super().__init__(name)
        self.tricks = 0

    # Override the parent method
    def summary(self):
        return f'{self.name} (dog) - {self.tricks} tricks'
```

---

## Second Subclass - Cat

```python
class Cat(Animal):
    # Cat inherits attributes and methods from Animal

    def __init__(self, name):
        # super() reuses the parent constructor
        super().__init__(name)
        self.naps = 0

    # Override the parent method
    def summary(self):
        return f'{self.name} (cat) - {self.naps} naps'
```

---

## Store Parent and Subclass Objects in One List

```python
animals = [
    Animal('Generic'),
    Dog('Rex'),
    Cat('Whiskers')
]
```

---

## Loop Through Every Object

```python
for a in animals:
    print(a.summary())
```

### Output

```text
Generic
Rex (dog) - 0 tricks
Whiskers (cat) - 0 naps
```

---

# Key Notes

## Class Modelling
- Identify **classes**, **attributes**, and **methods** before coding.
- **Nouns** → Classes / Attributes
- **Verbs** → Methods

## Objects
- An object is created from a class.
- Many objects can be stored inside a list.

## Methods
- Methods are functions inside a class.
- A method can call another method on the same object using `self`.

Example:

```python
rate = self.occupancy_rate()
```

## Best-So-Far Algorithm
1. Assume the first object is the best.
2. Compare every object with the current best.
3. If a better object is found, replace the current best.
4. After the loop, the variable `best` stores the best object.

## Inheritance
- A subclass inherits attributes and methods from its parent class.
- Use `super().__init__()` to reuse the parent constructor.
- A subclass can **override** a parent method by creating a method with the same name.
- Parent and subclass objects can be stored in the same list.
- When calling the same method (e.g. `summary()`), Python automatically uses the correct version for each object (**polymorphism**).
