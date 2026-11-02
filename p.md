# 🐍 Python OOP — Quick Revision Notes (Part 2)

### From Composition to Dependency Injection & Software Architecture

> **Purpose:** Composition, Aggregation, Association, Dependency Injection এবং এগুলোর বাস্তব ব্যবহার দ্রুত Revision করা।
>
> **Learning Path:** Composition → Aggregation → Association → Dependency Injection → Loose Coupling → Strategy & Routing → Multi-Agent Architecture

---

## 📑 সূচিপত্র

1. [Composition](#1-composition)
2. [Aggregation](#2-aggregation)
3. [Association](#3-association)
4. [Association vs Aggregation vs Composition](#4-association-vs-aggregation-vs-composition)
5. [return vs print — Return Propagation](#5-return-vs-print--return-propagation)
6. [Dependency Injection (DI)](#6-dependency-injection-di)
7. [Tight Coupling vs Loose Coupling](#7-tight-coupling-vs-loose-coupling)
8. [Dependency Injection-এর সুবিধা](#8-dependency-injection-এর-সুবিধা)
9. [Types of Dependency Injection](#9-types-of-dependency-injection)
10. [Strategy Pattern](#10-strategy-pattern)
11. [API Routing & Provider Switching](#11-api-routing--provider-switching)
12. [Multi-Agent Architecture](#12-multi-agent-architecture)
13. [Important Design Principles & Common Traps](#13-important-design-principles--common-traps)

---

# 1. Composition

## Definition

Composition হলো OOP-এর একটি Has-a Relationship, যেখানে একটি Object অন্য Object-এর ওপর Strong Ownership রাখে।

অর্থাৎ, একটি Object-এর মধ্যে অন্য Object-কে তার অংশ হিসেবে মডেল করা হয়।

## Example

```python
class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

car = Car()
car.start_car()
```

Output:

```text
Engine started!
```

## Explanation

```python
self.engine = Engine()
```

এখানে:

* `Car` Class-এর মধ্যে `Engine` Object তৈরি হচ্ছে।
* Engine Object-টি Car-এর attribute হিসেবে রাখা হচ্ছে।
* Car-এর একটি Engine আছে (Has-a Relationship)।
* Intended design অনুযায়ী Car তার Engine-এর ownership পরিচালনা করছে।

## Key Points

* Composition = Strong Ownership.
* এটি Has-a Relationship.
* একটি Class-এর Object অন্য Class-এর Object-কে নিজের অংশ হিসেবে ধারণ করে।
* Composition দিয়ে বড় Class-কে ছোট ছোট দায়িত্বে ভাগ করা যায়।
* Composition ব্যবহার করে একটি Class অন্য Class-এর Method ব্যবহার করতে পারে।

## Important Note

Python-এ Composition নিজে থেকে Object-এর Lifetime নিয়ন্ত্রণ করে না।

অন্য কোনো Reference থাকলে Container Object মুছে গেলেও তার অংশ হিসেবে ব্যবহৃত Object বেঁচে থাকতে পারে।

তাই Composition-এর মূল বিষয় হলো Design-এর Ownership Intent, শুধু Object কোথায় তৈরি হয়েছে তা নয়।

---

# 2. Aggregation

## Definition

Aggregation হলো Has-a Relationship-এর একটি দুর্বল Ownership-ভিত্তিক রূপ।

এখানে একটি Object অন্য Object-কে নিজের attribute হিসেবে ধরে রাখতে পারে, কিন্তু সেই Object-এর অস্তিত্ব Container Object-এর ওপর নির্ভরশীল নয়।

## Example

```python
class Teacher:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, teacher):
        self.teacher = teacher

teacher1 = Teacher("Rahim")

school1 = School(teacher1)

print(school1.teacher.name)
print(teacher1.name)
```

Output:

```text
Rahim
Rahim
```

## Explanation

```python
teacher1 = Teacher("Rahim")
school1 = School(teacher1)
```

এখানে:

* প্রথমে Teacher Object তৈরি হয়েছে।
* এরপর সেই Object-টি School-এর Constructor-এ পাঠানো হয়েছে।
* School সেটিকে নিজের `teacher` attribute-এ Reference হিসেবে সংরক্ষণ করেছে।

```python
self.teacher = teacher
```

এখানে নতুন Teacher তৈরি হয়নি।

বরং আগে থেকে থাকা Teacher Object-এর Reference সংরক্ষণ করা হয়েছে।

## Key Points

* Aggregation = Weak Ownership.
* এটি Has-a Relationship.
* একটি Object অন্য Object-এর Reference ধরে রাখতে পারে।
* দুইটি Object স্বাধীনভাবে থাকতে পারে।
* Container Object না থাকলেও অন্য Object স্বাধীনভাবে ব্যবহার করা সম্ভব হতে পারে।

## Important Note

Aggregation মানে একটি Object মুছে গেলে অন্য Object-এর কোনো প্রভাব পড়বে না, এমন নয়।

যেমন, School-এর Teacher Reference হারিয়ে গেলে School-এর কিছু কাজ ব্যাহত হতে পারে।

তবে Teacher-এর অস্তিত্ব School-এর ওপর নির্ভরশীল নয়।

---

# 3. Association

## Definition

যখন দুটি Independent Object একে অপরের সঙ্গে কোনো সম্পর্কের মাধ্যমে Interact করে, তখন সেই সম্পর্ককে Association বলা হয়।

এখানে Ownership বা Has-a Relationship থাকা বাধ্যতামূলক নয়।

## Real-Life Example

একজন Teacher একজন Student-কে পড়াচ্ছেন।

* Teacher একটি Independent Object.
* Student একটি Independent Object.
* Teacher Student-এর মালিক নন।
* Student-ও Teacher-এর অংশ নয়।
* তাদের মধ্যে Teaching Relationship রয়েছে।

## Python Example

```python
class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def teach(self, student):
        print(f"Teaching {student.name}")

student1 = Student("Sunny")
teacher1 = Teacher()

teacher1.teach(student1)
```

Output:

```text
Teaching Sunny
```

## Explanation

```python
def teach(self, student):
```

এখানে Student Object-টি শুধু Parameter হিসেবে গ্রহণ করা হয়েছে।

Teacher সেটিকে নিজের Attribute হিসেবে সংরক্ষণ করেনি।

দুটি Object স্বাধীনভাবে তৈরি হয়েছে এবং Method Call-এর মাধ্যমে Interact করছে।

## Key Points

* Association = Interacts with / Knows about.
* Ownership থাকা বাধ্যতামূলক নয়।
* Object দুটি Independent থাকতে পারে।
* একটি Object অন্য Object-কে Method Parameter হিসেবে গ্রহণ করতে পারে।
* Association-এর জন্য Inheritance প্রয়োজন হয় না।

---

# 4. Association vs Aggregation vs Composition

তিনটিই Object Relationship-এর ধারণা।

তবে Ownership এবং Dependency-এর ধরন আলাদা।

| Concept     | Relationship   | Ownership               | Example                            |
| ----------- | -------------- | ----------------------- | ---------------------------------- |
| Association | Interacts with | নির্দিষ্ট Ownership নেই | Teacher — Student                  |
| Aggregation | Has-a          | Weak Ownership          | Team — Player                      |
| Composition | Has-a          | Strong Ownership        | Computer — CPU (উদ্দেশ্য অনুযায়ী) |

## Visual Understanding

```text
Association:

Teacher -------- Student

দুটি Independent Object
তারা একে অপরের সঙ্গে Interact করে।

Aggregation:

Team ◇-------- Player

Team-এর Player আছে।
কিন্তু Player Team ছাড়াও থাকতে পারে।

Composition:

Computer ◆-------- CPU

Computer-এর CPU আছে।
Design অনুযায়ী CPU-কে Computer-এর অংশ হিসেবে
মডেল করা হয়েছে।
```

## Important Distinction

Aggregation এবং Composition-ও Association-এর বিশেষ ধরনের Relationship হিসেবে বিবেচিত হয়।

তাই এগুলো সম্পূর্ণ বিচ্ছিন্ন Concept নয়।

## Common Trap

শুধু নিচের Code দেখে Relationship নিশ্চিত করা যায় না:

```python
self.employee = employee
```

এটি শুধু একটি Object Reference সংরক্ষণ করছে।

Relationship Aggregation নাকি Composition, তা নির্ধারণ করতে Ownership এবং Design Intent বুঝতে হবে।

---

# 5. return vs print — Return Propagation

Composition শেখার সময় আমরা Method-এর Return Value নিয়ে আলোচনা করেছি।

## print()

`print()` কোনো Value প্রদর্শন করে।

```python
def show():
    print("Hello")

result = show()

print(result)
```

Output:

```text
Hello
None
```

কারণ `show()`-এর মধ্যে Explicit Return নেই।

তাই Python Implicitly `None` Return করে।

## return

`return` Function বা Method থেকে Value ফেরত দেয়।

```python
def get_message():
    return "Hello"

result = get_message()

print(result)
```

Output:

```text
Hello
```

## Return Propagation in Composition

```python
class Engine:
    def start(self):
        return "Engine started!"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        return self.engine.start()

car = Car()

result = car.start_car()

print(result)
```

Output:

```text
Engine started!
```

## Important Trap

যদি লিখি:

```python
def start_car(self):
    self.engine.start()
```

তাহলে Engine-এর Return Value বাইরে যাবে না।

কারণ Car-এর Method সেটি Return করেনি।

সঠিকভাবে Value Pass করতে:

```python
def start_car(self):
    return self.engine.start()
```

## Remember

* `print()` = Display a Value.
* `return` = Send a Value Back.
* কোনো Function Explicitly Return না করলে Python সাধারণত `None` Return করে।
* অন্য Method-এর Return Value বাইরে পাঠাতে চাইলে সেটি Return করতে হবে।

---

# 6. Dependency Injection (DI)

## Definition

Dependency Injection হলো একটি Design Technique, যেখানে কোনো Class তার প্রয়োজনীয় Dependency নিজে তৈরি না করে বাইরে থেকে গ্রহণ করে।

## Without Dependency Injection

```python
class Battery:
    def charge(self):
        print("Battery charging...")

class Phone:
    def __init__(self):
        self.battery = Battery()
```

এখানে Phone নিজেই Battery Object তৈরি করছে।

## With Dependency Injection

```python
class Battery:
    def charge(self):
        print("Battery charging...")

class Phone:
    def __init__(self, battery):
        self.battery = battery

battery1 = Battery()

phone1 = Phone(battery1)
```

এখানে Battery Object বাইরে তৈরি হয়েছে এবং Phone-এর Constructor-এ সরবরাহ করা হয়েছে।

## Main Difference

| Without DI                                 | With DI                               |
| ------------------------------------------ | ------------------------------------- |
| Phone নিজে Battery তৈরি করে                | Battery বাইরে তৈরি হয়                |
| Concrete Class-এর ওপর সরাসরি নির্ভরতা বেশি | Dependency বাইরে থেকে সরবরাহ করা যায় |
| পরিবর্তন করা তুলনামূলক কঠিন হতে পারে       | Implementation পরিবর্তন সহজ হতে পারে  |

## Remember

Dependency Injection হলো Dependency সরবরাহ করার পদ্ধতি।

এটি নিজে কোনো Has-a Relationship নয়।

---

# 7. Tight Coupling vs Loose Coupling

## Tight Coupling

যখন একটি Class অন্য একটি নির্দিষ্ট Class বা Implementation-এর ওপর শক্তভাবে নির্ভরশীল থাকে, তখন তাকে Tight Coupling বলা হয়।

Example:

```python
class NormalBattery:
    def charge(self):
        print("Normal charging...")

class Phone:
    def __init__(self):
        self.battery = NormalBattery()
```

এখানে Phone সরাসরি NormalBattery তৈরি করছে।

অন্য Battery ব্যবহার করতে চাইলে Phone-এর Code পরিবর্তন করতে হবে।

## Loose Coupling

যখন একটি Class অন্য নির্দিষ্ট Implementation-এর ওপর কম নির্ভরশীল থাকে, তখন তাকে Loose Coupling বলা হয়।

Example:

```python
class NormalBattery:
    def charge(self):
        print("Normal charging...")

class FastBattery:
    def charge(self):
        print("Fast charging...")

class Phone:
    def __init__(self, battery):
        self.battery = battery

    def charge_phone(self):
        self.battery.charge()

normal = NormalBattery()
fast = FastBattery()

phone1 = Phone(normal)
phone2 = Phone(fast)

phone1.charge_phone()
phone2.charge_phone()
```

Output:

```text
Normal charging...
Fast charging...
```

এখানে Phone Class পরিবর্তন না করেই Battery পরিবর্তন করা যাচ্ছে।

## Remember

* Tight Coupling = বেশি নির্ভরশীলতা।
* Loose Coupling = কম নির্ভরশীলতা।
* Dependency Injection Loose Coupling তৈরি করতে সাহায্য করতে পারে।
* তবে Dependency Injection ব্যবহার করলেই স্বয়ংক্রিয়ভাবে সম্পূর্ণ Loose Coupling তৈরি হয় না।
* Abstraction, Interface বা Protocol ব্যবহার করলে Coupling আরও কমানো যায়।

---

# 8. Dependency Injection-এর সুবিধা

## 1. Flexibility

একই Class-এর সঙ্গে বিভিন্ন Implementation ব্যবহার করা যায়।

```python
phone1 = Phone(NormalBattery())
phone2 = Phone(FastBattery())
```

## 2. Reusability

একটি Class বিভিন্ন Dependency-এর সঙ্গে Reuse করা যায়।

## 3. Testability

Testing-এর সময় Real Dependency-এর পরিবর্তে Fake বা Mock Object ব্যবহার করা যায়।

Example:

```python
class FakeBattery:
    def charge(self):
        print("Testing battery...")

test_phone = Phone(FakeBattery())

test_phone.charge_phone()
```

Output:

```text
Testing battery...
```

## 4. Maintainability

Dependency পরিবর্তন হলে মূল Class-এর Code বারবার পরিবর্তন করতে হয় না।

## Remember

Dependency Injection Software-কে আরও:

* Flexible
* Reusable
* Testable
* Maintainable

করতে সাহায্য করে।

---

# 9. Types of Dependency Injection

Dependency Injection-এর কয়েকটি প্রচলিত পদ্ধতি রয়েছে।

| Type                  | Description                                               |
| --------------------- | --------------------------------------------------------- |
| Constructor Injection | Constructor-এর মাধ্যমে Dependency সরবরাহ করা              |
| Setter Injection      | আলাদা Setter Method দিয়ে Dependency সরবরাহ করা           |
| Method Injection      | নির্দিষ্ট Method-এর Argument হিসেবে Dependency সরবরাহ করা |

## 1. Constructor Injection

```python
class Phone:
    def __init__(self, battery):
        self.battery = battery

phone = Phone(Battery())
```

Object তৈরি করার সময় Dependency দেওয়া হয়েছে।

## 2. Setter Injection

```python
class Phone:
    def set_battery(self, battery):
        self.battery = battery

phone = Phone()

phone.set_battery(Battery())
```

আলাদা Method দিয়ে Dependency সরবরাহ করা হয়েছে।

## 3. Method Injection

```python
class Phone:
    def charge(self, battery):
        battery.charge()

phone = Phone()

phone.charge(Battery())
```

নির্দিষ্ট Method Call করার সময় Dependency দেওয়া হয়েছে।

---

# 10. Strategy Pattern

## Definition

Strategy Pattern হলো একটি Behavioral Design Pattern।

এখানে একই কাজ সম্পন্ন করার জন্য একাধিক Algorithm বা Strategy রাখা হয় এবং প্রয়োজন অনুযায়ী একটি Strategy নির্বাচন করা হয়।

## Example

ধর, একটি Payment System আছে।

```python
class CashPayment:
    def pay(self, amount):
        print("Paid by cash:", amount)

class CardPayment:
    def pay(self, amount):
        print("Paid by card:", amount)

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

cash = PaymentProcessor(CashPayment())

card = PaymentProcessor(CardPayment())

cash.process(500)
card.process(1000)
```

Output:

```text
Paid by cash: 500
Paid by card: 1000
```

## Key Points

* Strategy Pattern বিভিন্ন Implementation আলাদা রাখে।
* Runtime-এ Strategy পরিবর্তন করা সম্ভব।
* Dependency Injection দিয়ে Strategy সরবরাহ করা যায়।
* একই Class-কে বিভিন্ন Behavior দেওয়া যায়।

## DI vs Strategy Pattern

| Dependency Injection             | Strategy Pattern                      |
| -------------------------------- | ------------------------------------- |
| Dependency সরবরাহ করার Technique | Behavior পরিবর্তনের Design Pattern    |
| Object কীভাবে Dependency পাবে    | কোন Algorithm বা Strategy ব্যবহার হবে |

দুটি একসঙ্গে ব্যবহার করা যায়।

---

# 11. API Routing & Provider Switching

এটি AI/ML Software Development-এর জন্য গুরুত্বপূর্ণ একটি ব্যবহারিক উদাহরণ।

ধর, একটি AI Assistant কখনো Groq API এবং কখনো Gemini API ব্যবহার করবে।

প্রতিটি Provider-এর জন্য আলাদা Class তৈরি করা যায়।

## Step 1: Provider Classes

```python
class GroqProvider:
    def generate(self, prompt):
        return "Answer from Groq"

class GeminiProvider:
    def generate(self, prompt):
        return "Answer from Gemini"
```

## Step 2: Main Assistant

```python
class Assistant:
    def __init__(self, provider):
        self.provider = provider

    def ask(self, prompt):
        return self.provider.generate(prompt)
```

## Step 3: Dependency Injection

```python
assistant1 = Assistant(GroqProvider())

assistant2 = Assistant(GeminiProvider())

print(assistant1.ask("Explain AI"))
print(assistant2.ask("Explain AI"))
```

Output:

```text
Answer from Groq
Answer from Gemini
```

এখানে Assistant Class পরিবর্তন না করেই Provider পরিবর্তন করা যাচ্ছে।

## API Routing

Task অনুযায়ী Provider নির্বাচন করার জন্য Router ব্যবহার করা যায়।

```python
class AIRouter:
    def choose_provider(self, task):

        if task == "complex":
            return GeminiProvider()

        return GroqProvider()
```

ব্যবহার:

```python
router = AIRouter()

provider = router.choose_provider("complex")

assistant = Assistant(provider)

print(assistant.ask("Solve this problem"))
```

## Conceptual Flow

```text
User Task
    |
    v
AI Router
    |
    |--- Regular Task ---> Groq
    |
    |--- Complex Task ---> Gemini
    |
    v
Assistant
    |
    v
Final Response
```

## Important Points

* Dependency Injection = Provider সরবরাহ করা।
* Routing = কোন Provider ব্যবহার হবে তা নির্বাচন করা।
* Strategy Pattern = Provider-এর বিভিন্ন Implementation ব্যবহার করা।
* বাস্তবে Task Complexity ছাড়াও Cost, Latency, Context Window, Model Capability, Tool Support এবং API Availability বিবেচনা করতে হয়।

## Important Warning

শুধু "Complex" এবং "Normal" শর্ত দিয়ে বাস্তব Model Selection করা যথেষ্ট নয়।

এটি একটি Simplified Example।

---

# 12. Multi-Agent Architecture

## Definition

Multi-Agent System হলো এমন একটি Architecture, যেখানে একাধিক AI Agent একসঙ্গে বা সমন্বিতভাবে কোনো Task সম্পন্ন করে।

প্রতিটি Agent-এর আলাদা Role থাকতে পারে।

## Example Architecture

```text
              User Task
                  |
                  v
           Leader / Orchestrator
                  |
        __________|__________
       |          |          |
       v          v          v
   Research    Coding     Reviewer
    Agent       Agent       Agent
       |          |          |
       |__________|__________|
                  |
                  v
          Leader / Orchestrator
                  |
                  v
            Final Response
```

## Possible Agent Roles

| Agent                 | Responsibility                  |
| --------------------- | ------------------------------- |
| Leader / Orchestrator | Task ভাগ করা এবং Agent পরিচালনা |
| Research Agent        | তথ্য সংগ্রহ ও বিশ্লেষণ          |
| Coding Agent          | Code লেখা ও পরীক্ষা             |
| Reviewer Agent        | ফলাফল যাচাই করা                 |

## Dependency Injection-এর সঙ্গে সম্পর্ক

প্রতিটি Agent-কে আলাদা AI Provider সরবরাহ করা যেতে পারে।

Example:

| Agent          | Provider      |
| -------------- | ------------- |
| Research Agent | Gemini        |
| Coding Agent   | Groq          |
| Reviewer Agent | অন্য Provider |

Dependency Injection ব্যবহার করে Agent-দের Provider বা অন্যান্য Service সরবরাহ করা যায়।

## Important Distinction

Dependency Injection নিজে Agent-দের কাজ ভাগ করে দেয় না।

Agent-এর কাজ ভাগ করা, তাদের Execution পরিচালনা করা এবং ফলাফল একত্র করার দায়িত্ব Orchestrator বা Agent Workflow-এর।

## Important Warning

Multi-Agent System সবসময় Single-Agent System-এর চেয়ে ভালো নয়।

সম্ভাব্য সমস্যা:

* বেশি API Cost
* বেশি Latency
* Debugging-এর জটিলতা
* Agent-দের মধ্যে ভুল Communication
* ভুল সিদ্ধান্ত এক Agent থেকে অন্য Agent-এ ছড়িয়ে পড়া

তাই আগে ভালো Single-Agent System তৈরি করা গুরুত্বপূর্ণ।

---

# 13. Important Design Principles & Common Traps

* Composition = Strong Ownership.
* Aggregation = Weak Ownership.
* Association = Interaction / Relationship.
* Aggregation ও Composition Association-এর বিশেষ রূপ হিসেবে বিবেচিত হতে পারে।
* শুধু `self.object = object` দেখে Relationship নিশ্চিত করা যায় না।
* Ownership ও Design Intent বিবেচনা করতে হয়।
* Python-এ Composition-এর জন্য আলাদা Keyword নেই।
* Python নিজে Composition ও Aggregation-এর Lifetime Enforce করে না।
* Dependency Injection = Dependency বাইরে থেকে সরবরাহ করা।
* Dependency Injection এবং Aggregation একই Concept নয়।
* Constructor Injection সবচেয়ে পরিচিত DI Technique।
* Loose Coupling Software-কে পরিবর্তনযোগ্য করতে সাহায্য করে।
* Dependency Injection ব্যবহার করলেই সব Coupling দূর হয় না।
* Strategy Pattern বিভিন্ন Behavior বা Algorithm পরিবর্তন করতে সাহায্য করে।
* API Routing নির্ধারণ করে কোন Provider বা Model ব্যবহার হবে।
* Multi-Agent Architecture-এ একাধিক Agent কাজ ভাগ করে করতে পারে।
* Orchestrator Agent পরিচালনা করে; Dependency Injection শুধু Dependency সরবরাহ করে।
* Multi-Agent System সবসময় Single-Agent System-এর চেয়ে ভালো নয়।
