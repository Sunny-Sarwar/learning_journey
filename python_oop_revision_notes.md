# 🐍 Python OOP — Quick Revision Notes

### From Polymorphism to Operator Overloading

> **Purpose:** Composition শেখার আগে দ্রুত revision
> **Language:** Python
> **Learning Path:** Encapsulation & Inheritance → Polymorphism → Duck Typing → Operator Overloading

---

## 📑 সূচিপত্র

1. [OOP Foundation: Quick Recap](#1-oop-foundation-quick-recap)
2. [Polymorphism](#2-polymorphism)
3. [Duck Typing](#3-duck-typing)
4. [`self` and `other`](#4-self-and-other)
5. [Special Methods / Dunder Methods](#5-special-methods--dunder-methods)
6. [Operator Overloading](#6-operator-overloading)
7. [Common Traps to Remember](#7-common-traps-to-remember)
8. [Mastery Check — Quick Questions (উত্তরসহ)](#8-mastery-check--quick-questions-উত্তরসহ)

---

## 1. OOP Foundation: Quick Recap

### Class and Object

| Term | অর্থ |
|---|---|
| **Class** | Object তৈরির blueprint |
| **Object** | Class থেকে তৈরি একটি instance |
| **Attribute** | Object-এর সঙ্গে যুক্ত data বা বৈশিষ্ট্য |
| **Method** | Class-এর মধ্যে সংজ্ঞায়িত function, যা object-এর সঙ্গে কাজ করে |

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name}"


s = Student("Sunny")

print(s.name)        # Sunny
print(s.introduce()) # I'm Sunny
```

### `self` and `__init__()`

- `self` বর্তমান instance-কে reference করে।
- `__init__()` object তৈরি হওয়ার পর তার initial state সেট করে।
- `self.name = name` দিয়ে instance attribute তৈরি করা হয়েছে।

### Attribute vs Method

```python
s.name         # Attribute access
s.introduce()  # Method call
```

> 💡 **মনে রাখবে:**
> - Attribute = Object-এর **data**
> - Method = Object-এর **কাজ**

### `return` vs `print()`

- `print()` কোনো value **প্রদর্শন** করে।
- `return` function বা method থেকে value **ফেরত** দেয়।

```python
def get_name():
    return "Sunny"

name = get_name()
print(name)  # Sunny
```

---

## 2. Polymorphism

**Polymorphism** অর্থ একই interface বা method call বিভিন্ন object-এর ক্ষেত্রে বিভিন্ন behavior দেখাতে পারে।

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.speak()  # Woof!
cat.speak()  # Meow!
```

এখানে `Dog` ও `Cat` একই `speak()` method ব্যবহার করলেও তাদের behavior আলাদা।

### Method Overriding

Child class-এ parent class-এর method-এর নিজস্ব implementation দেওয়া হলে তাকে **Method Overriding** বলে।

```python
class Parent:
    def greet(self):
        print("Hello from Parent")


class Child(Parent):
    def greet(self):
        print("Hello from Child")
```

`Child`-এর object থেকে `greet()` call করলে child class-এর implementation ব্যবহার হবে।

### Inheritance vs Overriding vs Polymorphism

| Concept | অর্থ |
|---|---|
| **Inheritance** | Parent class থেকে behavior ও attributes পাওয়া |
| **Overriding** | Child class-এ inherited method-এর নতুন implementation দেওয়া |
| **Polymorphism** | একই interface ব্যবহার করে বিভিন্ন behavior পাওয়া |

> 💡 **মনে রাখবে:** Inheritance ব্যবহার করে polymorphism তৈরি করা যায়, কিন্তু polymorphism-এর জন্য সবসময় inheritance প্রয়োজন হয় না।

---

## 3. Duck Typing

Python-এর Duck Typing ধারণা:

> কোনো object কোন class-এর, শুধু সেটা না দেখে object-টি প্রয়োজনীয় behavior দিতে পারে কি না, সেটিও বিবেচনা করা হয়।

```python
class Dog:
    def speak(self):
        print("Woof!")


class Robot:
    def speak(self):
        print("Beep!")


def make_it_speak(thing):
    thing.speak()


make_it_speak(Dog())    # Woof!
make_it_speak(Robot())  # Beep!
```

এখানে `Dog` ও `Robot`-এর মধ্যে inheritance নেই। তবুও দুটিই কাজ করছে, কারণ দুটিরই `speak()` method আছে।

### ⚠️ Missing Method Trap

```python
class Button:
    def press(self):
        print("Button pressed!")


def activate(device):
    device.click()


activate(Button())  # AttributeError
```

**কেন error?**
`Button` class-এ `click()` নেই। শুধু `press()` থাকলে Python নিজে থেকে বুঝবে না যে `press()` ও `click()` একই কাজ বোঝায়।

### Duck Typing-এর মূল কথা

- Inheritance থাকা **বাধ্যতামূলক নয়**।
- প্রয়োজনীয় method বা behavior **থাকতে হবে**।
- প্রয়োজনীয় attribute বা method না থাকলে **runtime error** হতে পারে।

---

## 4. `self` and `other`

`self` এবং `other` হলো method-এর **parameter name**; `other` কোনো Python keyword নয়।

```python
class Player:
    def __init__(self, score):
        self.score = score

    def compare(self, other):
        return self.score + other.score


p1 = Player(40)
p2 = Player(60)

print(p1.compare(p2))  # 100
```

`p1.compare(p2)` call করার সময়:

| Parameter | কোন object |
|---|---|
| `self` | `p1` |
| `other` | `p2` |

অর্থাৎ, dot-এর আগে থাকা object সাধারণ instance method-এ `self` হিসেবে যায়, আর argument হিসেবে পাঠানো object `other`-এ যায়।

> নামের পরিবর্তে এখানে reference ও object-এর **ভূমিকা** বোঝাটাই বেশি গুরুত্বপূর্ণ।

---

## 5. Special Methods / Dunder Methods

যেসব special method-এর নাম সাধারণত **double underscore** দিয়ে শুরু ও শেষ হয়, সেগুলোকে প্রায়ই **dunder methods** বলা হয়।

**উদাহরণ:**

- `__init__()`
- `__str__()`
- `__repr__()`
- `__add__()`
- `__eq__()`
- `__lt__()`

Python-এর built-in operations এসব method-এর নির্ধারিত protocol অনুসরণ করে object-এর সঙ্গে কাজ করতে পারে।

---

## 6. Operator Overloading

**Operator Overloading** হলো নিজের class-এর object-এর জন্য operator কীভাবে কাজ করবে তা নির্ধারণ করা।

যেমন, `+` operator দিয়ে দুটি `Box` object যোগ করার নিয়ম আমরা নিজেরাই নির্ধারণ করতে পারি।

### 6.1 `__add__()` — `+` Operator

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


box1 = Box(10)
box2 = Box(25)

print(box1 + box2)  # 35
```

`box1 + box2` expression-এর জন্য Python `__add__()`-এর মতো special-method protocol ব্যবহার করে।

**Conceptually:**

```python
box1.__add__(box2)
```

| Name | Value |
|---|---|
| `self` | `box1` |
| `other` | `box2` |
| `self.value` | `10` |
| `other.value` | `25` |

তাই return value হলো integer `35`।

> ⚠️ **গুরুত্বপূর্ণ:** উপরের explicit method call-টি বোঝার সুবিধার জন্য। বাস্তবে operator dispatch-এর কিছু অতিরিক্ত নিয়ম আছে, যেমন reflected method ও fallback।

### 6.2 Integer Return vs Object Return

**Integer return:**

```python
def __add__(self, other):
    return self.value + other.value
```

এতে যোগফল **integer** হিসেবে ফেরত আসে।

**নতুন object return:**

```python
def __add__(self, other):
    return Box(self.value + other.value)
```

এতে একটি নতুন `Box` object তৈরি হয়ে return হয়।

```python
box1 = Box(12)
box2 = Box(8)

result = box1 + box2

print(result.value)  # 20
```

এখানে `result` নতুন object-টিকে reference করে। `result` object-এর নাম নয়; এটি **variable-এর নাম**।

### 6.3 `__str__()` — Readable Representation

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Box({self.value})"


box = Box(12)

print(box)        # Box(12)
print(box.value)  # 12
```

- `print(box)` সাধারণত `__str__()` ব্যবহার করে।
- `print(box.value)` সরাসরি attribute-এর value প্রদর্শন করে।
- `__str__()`-এর return value অবশ্যই **string** হতে হবে।

`__str__()` না থাকলে `print(object)` সাধারণত error না দিয়ে default representation দেখায়।

### 6.4 `__repr__()` — Debugging Representation

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Box(value={self.value})"


box = Box(12)

print(repr(box))  # Box(value=12)
```

| Method | উদ্দেশ্য |
|---|---|
| `__str__()` | মানুষের পড়ার উপযোগী representation |
| `__repr__()` | Debugging ও object-এর স্পষ্ট representation |

`__str__()` না থাকলে Python অনেক ক্ষেত্রে `__repr__()`-এ fallback করতে পারে।

### 6.5 `__eq__()` — `==` Operator

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


a = Box(10)
b = Box(10)
c = Box(25)

print(a == b)  # True
print(a == c)  # False
```

আমরা এখানে object identity নয়, বরং `value` তুলনা করার নিয়ম নির্ধারণ করেছি।

> 💡 **মনে রাখবে:** দুটি object আলাদা হলেও `__eq__()` তাদের সমান বলে বিবেচনা করতে পারে।
> বাস্তব code-এ `other`-এর type যাচাই করার প্রয়োজন হতে পারে।

### 6.6 `__lt__()` — `<` Operator

`lt` অর্থ *less than*।

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


a = Box(10)
b = Box(25)

print(a < b)  # True
print(b < a)  # False
```

এখানে object-এর `value` তুলনা করা হয়েছে।

### 6.7 আরও কিছু Operator Methods

| Operator | Special method |
|---|---|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |
| `+=`-এর in-place behavior | `__iadd__()` |

> সবগুলো মুখস্থ করা জরুরি নয়। Operator অনুযায়ী method-এর নাম reference দেখে মনে করে নেওয়া যায়।

### 6.8 `__iadd__()` — `+=`

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        self.value += amount
        return self


counter = Counter(10)
counter += 5

print(counter.value)  # 15
```

এখানে `__iadd__()` বর্তমান object-এর `value` পরিবর্তন করেছে এবং `self` return করেছে।

> ⚠️ **সতর্কতা:** `+=` সবসময় object-এর ভেতরের data পরিবর্তন করে—এমন নয়। `__iadd__()` না থাকলে Python অন্যান্য উপযুক্ত operator method-এ fallback করতে পারে।

---

## 7. Common Traps to Remember

1. `other` **keyword নয়**। এটি method parameter-এর সাধারণ নাম।
2. **Inheritance ছাড়া Duck Typing সম্ভব।** প্রয়োজনীয় behavior থাকলেই যথেষ্ট হতে পারে।
3. `return` নিজে থেকে `print()` করে না।
4. `result` **variable**, object-এর নাম নয়। এটি object-টিকে reference করে।
5. `return 20` ও `return Box(20)` এক নয়। একটি integer, অন্যটি `Box` object।
6. `print(object)` এবং `print(object.value)` এক নয়।
7. `__str__()`-এর return value **string** হতে হবে।
8. `==`-এর অর্থ class-এর `__eq__()` implementation-এর ওপর নির্ভর করতে পারে।
9. `__add__()` rename করে `add()` করলে `+` স্বয়ংক্রিয়ভাবে `add()` call করবে না।
10. Operator Overloading মানে operator-এর **behavior** নির্ধারণ করা; operator-এর **syntax** বদলে ফেলা নয়।

---

## 8. Mastery Check — Quick Questions (উত্তরসহ)

### Q1
`__add__()`-এ যদি `return self.value + other.value` থাকে, তাহলে return type কী হবে?

**✅ উত্তর:** Return type হবে `self.value + other.value`-এর ফলাফলের type। `value` দুটি integer হলে return type **`int`** (যেমন `Box(10) + Box(25)` → `35`)। এটি `Box` object নয়, সাধারণ integer।

---

### Q2
যদি `__add__()` `return Box(self.value + other.value)` করে, তাহলে `result.value` কীভাবে পাওয়া যাবে?

**✅ উত্তর:** যোগ করলে একটি **নতুন `Box` object** পাওয়া যায়। সেটি variable-এ রেখে `.value` দিয়ে data পড়তে হয়:

```python
result = box1 + box2   # নতুন Box object
print(result.value)    # যোগফল
```

---

### Q3
Inheritance না থাকলেও দুটি class-এর object একই function-এ কাজ করতে পারে কোন concept-এর মাধ্যমে?

**✅ উত্তর:** **Duck Typing**-এর মাধ্যমে। দুটি class-এর মধ্যে inheritance না থাকলেও, দুটিরই প্রয়োজনীয় method (যেমন `speak()`) থাকলে একই function-এ কাজ করে।

---

### Q4
`print(box)` এবং `print(box.value)`-এর পার্থক্য কী?

**✅ উত্তর:**

| Code | কী print হয় |
|---|---|
| `print(box)` | পুরো object-এর representation। `__str__()` থাকলে সেটি ব্যবহার হয় (যেমন `Box(12)`); না থাকলে default representation |
| `print(box.value)` | object-এর ভেতরের `value` attribute-এর মান (যেমন `12`) |

---

### Q5
`a == b`-এর behavior নিজের class অনুযায়ী নির্ধারণ করতে কোন special method ব্যবহার করা হয়?

**✅ উত্তর:** **`__eq__()`** method।

---

### Q6
`self` ও `other`-এর মধ্যে পার্থক্য কী?

**✅ উত্তর:** `a.method(b)` call-এ:

- `self` → dot-এর **আগের** object (`a`), অর্থাৎ যে object-এর ওপর method call হচ্ছে।
- `other` → argument হিসেবে পাঠানো **অন্য** object (`b`)।

দুটিই কেবল parameter-এর নাম, keyword নয়। নাম বদলালেও ভূমিকা একই থাকে।

---

### Q7
`__str__()` ও `__repr__()`-এর মূল উদ্দেশ্য কী?

**✅ উত্তর:**

- `__str__()` → মানুষের জন্য **readable** representation (যেমন `print()`-এ দেখানোর জন্য)।
- `__repr__()` → **debugging** ও object-এর স্পষ্ট, নির্ভুল representation-এর জন্য।

---

> 🎯 **Revision principle:** শুধু definition মুখস্থ নয়—প্রতিটি concept-এর code predict করো, নিজে code লেখো, error তৈরি করে debug করো, এবং নিজের ভাষায় explain করো।

*End of Quick Revision Notes*
