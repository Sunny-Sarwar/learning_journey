# 🐍 Python OOP — Encapsulation & Inheritance

**Quick Revision Notes**

---

## 🔐 1. Encapsulation

### 💡 What is Encapsulation?

**Encapsulation** = Data + সেই data-এর উপর কাজ করার methods-কে একসাথে রাখা এবং data access/control করার ব্যবস্থা করা।

সহজভাবে:

> “Data-কে class-এর ভিতরে রাখো, আর দরকার হলে controlled way-তে access/change করতে দাও।”

### Mental Model

```text
                 CLASS
        ┌─────────────────────┐
        │  Data               │
        │  _balance           │
        │                     │
        │  Methods            │
        │  deposit()          │
        │  withdraw()         │
        │  show_balance()     │
        └─────────────────────┘
                  ↑
          Controlled access
```

---

### 🧱 Basic Example

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def show_balance(self):
        return self._balance

account = BankAccount(1000)

account.deposit(500)

print(account.show_balance())
# 1500
```

এখানে:

- `_balance` → internal data
- `deposit()` → balance পরিবর্তনের controlled way
- `show_balance()` → balance দেখার way

---

### `_` এবং `__`

#### 1️⃣ Normal attribute

```python
self.balance = balance
```

এটি সাধারণ attribute।

#### 2️⃣ Single underscore `_`

```python
self._balance = balance
```

`_balance` Python-এর private keyword নয়।

এটি একটি **convention**:

> “এই attribute-টা internal; বাইরে থেকে সরাসরি ব্যবহার না করাই ভালো।”

কিন্তু Python আটকাবে না:

```python
account._balance = 999999
```

তাই `_` কোনো security system নয়।

#### 3️⃣ Double underscore `__`

```python
self.__balance = balance
```

এখানে Python **name mangling** করে।

যেমন:

```python
self.__balance
```

internally roughly:

```python
self._BankAccount__balance
```

তাই:

```python
account.__balance
```

সরাসরি সাধারণত কাজ করবে না।

> ⚠️ এটাও absolute security নয়।

---

### 🏷️ `@property`

`@property` ব্যবহার করলে method-কে attribute-এর মতো ব্যবহার করা যায়।

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
```

এখন:

```python
account.balance
```

লিখলেই getter method automatically call হবে।

`account.balance()` লিখতে হবে না।

---

### ✏️ Property Setter

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Balance cannot be negative!")
```

এখন:

```python
account.balance = 500
```

লিখলে setter automatically call হবে।

**Flow:**

```text
account.balance
       ↓
    getter
       ↓
 self._balance
```

আর —

```text
account.balance = 500
       ↓
    setter
       ↓
 validation
       ↓
 self._balance = 500
```

#### ⭐ মনে রাখো

```text
@property
    ↓
Getter

@property_name.setter
    ↓
Setter
```

---

### 🔑 Encapsulation-এর Core Idea

```text
Raw data
   ↓
Class-এর ভিতরে রাখা
   ↓
Methods / properties দিয়ে controlled access
   ↓
Validation + protection + clean interface
```

**Golden Rule:**

> Encapsulation মানে শুধু “data hide করা” নয়; data এবং behavior একসাথে রেখে access/control করা।

---

## 🧬 2. Inheritance

### 💡 What is Inheritance?

**Inheritance** = একটি class অন্য class-এর attributes এবং methods reuse/extend করতে পারে।

অর্থাৎ:

> Child class → Parent class-এর existing functionality পায়।

---

### 🌳 Basic Structure

```text
        Animal
       /      \
     Dog      Cat
```

এখানে:

- `Animal` → Parent / Superclass / Base class
- `Dog` → Child / Subclass / Derived class
- `Cat` → Child / Subclass / Derived class

---

### 🧱 Basic Example

```python
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.eat()
dog.bark()
```

**Output:**

```text
Animal is eating
Dog is barking
```

কেন?

`Dog` `Animal` থেকে inherit করেছে।

তাই `Dog` নিজের `bark()`-এর পাশাপাশি parent-এর `eat()`-ও ব্যবহার করতে পারে।

---

### 🔍 Method Lookup

যখন লিখি:

```python
dog.speak()
```

Python roughly:

```text
        dog.speak()
             ↓
       Dog class-এ খোঁজে
             ↓
        পাওয়া গেল?
        /          \
      YES           NO
       ↓             ↓
   Dog-এর       Parent class
    method        এ খোঁজে
                    ↓
              Animal.speak()
```

**Golden Rule:**

> Child class-এ method না পেলে Python parent class-এ খোঁজে।

---

### 🏗️ Inheritance + `__init__`

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Bruno", "German Shepherd")
```

এখন:

```python
print(dog.name)
# Bruno

print(dog.breed)
# German Shepherd
```

---

### 🚀 `super()`

`super()` ব্যবহার করে সাধারণত parent class-এর functionality call করা হয়।

```python
super().__init__(name)
```

এর অর্থ:

> “Parent class-এর `__init__()` চালাও।”

#### Mental Model

```text
Dog.__init__()
      │
      ├── super().__init__(name)
      │          ↓
      │    Animal.__init__()
      │          ↓
      │      self.name
      │
      └── self.breed
```

---

### 🔄 Method Overriding

যখন child class parent-এর একই নামের method নিজের version দিয়ে redefine করে, তখন তাকে **method overriding** বলে।

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Cat(Animal):
    def speak(self):
        print("Meow")
```

এখন:

```python
cat = Cat()
cat.speak()
```

**Output:**

```text
Meow
```

কারণ `Cat` নিজের `speak()` লিখেছে।

---

### 🧠 Inheritance vs Overriding

> এটা খুব গুরুত্বপূর্ণ!

**Dog:**

```python
class Dog(Animal):
    pass

dog.speak()
```

যদি `Dog`-এ `speak()` না থাকে:

```text
Dog
 ↓
কোনো speak নেই
 ↓
Animal
 ↓
Animal.speak()
```

এটা **inheritance**।

**Cat:**

```python
class Cat(Animal):
    def speak(self):
        print("Meow")
```

এখানে:

```text
Animal.speak()
       ↓
   Cat.speak()
```

Child নিজের একই নামের method দিয়েছে।

এটা **method overriding**।

---

### ⚡ Inheritance + Overriding Together

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```

**Output:**

```text
Woof
Meow
```

এখানে:

- `Dog` → `Animal` থেকে inherit করেছে
- `Cat` → `Animal` থেকে inherit করেছে
- `Dog.speak()` → override
- `Cat.speak()` → override

---

## 🧩 Important OOP Vocabulary

| Term | Meaning |
|---|---|
| Parent class | যে class থেকে inherit করা হয় |
| Child class | যে class inherit করে |
| Superclass | Parent class |
| Subclass | Child class |
| Base class | Parent class |
| Derived class | Child class |
| Inheritance | Parent-এর functionality পাওয়া |
| Method overriding | Child-এর একই নামের নতুন method |
| `super()` | Parent functionality access করার উপায় |

---

## ⚠️ Common Traps

❌ **ভুল:**

> “Dog-এর `speak()` নেই, তাই Dog overriding করেছে।”

✅ **ঠিক:**

> Dog-এর `speak()` নেই, তাই সে parent-এর `speak()` inherit করেছে।

---

❌ **ভুল:**

> “`super()` object তৈরি করে।”

✅ **ঠিক:**

> `super()` parent class-এর functionality access করতে সাহায্য করে।

---

❌ **ভুল:**

> “`__init__` object তৈরি করে।”

✅ **ঠিক:**

> Object তৈরি হওয়ার পর `__init__` object-টাকে initialize করে।

---

❌ **ভুল:**

> “`_balance` private এবং কেউ access করতে পারবে না।”

✅ **ঠিক:**

> `_balance` একটি convention—Python technically access আটকায় না।

---

## 🧠 10-Second Revision

### Encapsulation

```text
Data + Methods
      ↓
এক class-এর ভিতরে
      ↓
Controlled access
```

Important tools:

```text
_balance
__balance
@property
@setter
```

---

### Inheritance

```text
Parent
  ↓
Child
```

Child parent-এর functionality reuse করতে পারে।

```python
class Dog(Animal):
    pass
```

---

### `super()`

```python
super().__init__(...)
```

→ Parent-এর `__init__()` call করার common way।

---

### Method Overriding

```text
Parent:
    speak()

Child:
    speak()
```

Child-এর version → parent-এর version-এর বদলে child object-এর ক্ষেত্রে ব্যবহৃত হয়।

---

## 🏆 Final Mental Model

```text
                    OOP
                     │
          ┌──────────┴──────────┐
          │                     │
   Encapsulation           Inheritance
          │                     │
   Data + Methods          Parent → Child
          │                     │
    Controlled access      Reuse / Extend
          │                     │
   ┌──────┴──────┐       ┌──────┴───────┐
   │             │       │              │
 _data       @property  super()     overriding
   │
 __data
```

### ⭐ দুইটি Golden Rule

**Encapsulation:**

> “Data-কে শুধু রাখব না—কীভাবে access/change হবে সেটাও control করব।”

**Inheritance:**

> “যা parent-এর আছে, child সেটা reuse করতে পারে; আর চাইলে নিজের version দিয়ে override করতে পারে।”
