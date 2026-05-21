# 📓 Complete Study Notes
### Python · Developer's Toolkit · Software Engineering
## 🐍 Part 1 — Python Basics
 
### 01. input() — তথ্য নেওয়া
 
| Type | Use | Code |
|------|-----|------|
| String | Text / yes/no | `name = input("Name: ")` |
| Integer | বয়স / marks | `age = int(input("Age: "))` |
| Float | CGPA / bill | `cgpa = float(input("CGPA: "))` |
 
> ⚠️ `input()` সবসময় **string** দেয় — সংখ্যার জন্য `int()` বা `float()` দিয়ে convert করো।  
> ✅ `.lower()` যোগ করো — "YES" / "yes" / "Yes" সব একসাথে handle হবে।
 
---
 
### 02. if / elif / else — শর্ত
 
```python
if শর্ত১:
    # শর্ত১ True হলে
elif শর্ত২:
    # শর্ত২ True হলে
else:
    # কোনোটাই না হলে
```
 
**Grade System উদাহরণ:**
```python
marks = float(input("Marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("F")
```
 
> ⚠️ শর্তের পরে `:` দিতে হবে।  
> ⚠️ ভেতরে **4 space** (indentation) দিতে হবে।  
> ⚠️ `else`-এ কোনো condition লেখা যায় না!
 
---
 
### 03. Ternary Operator — এক লাইনে if/else
 
```python
value = "A" if শর্ত else "B"
```
 
**উদাহরণ:**
```python
age = int(input("Age: "))
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)
```
 
| পরিস্থিতি | কোনটি ব্যবহার করবো |
|-----------|-------------------|
| ২টি option (if/else) | ✅ Ternary |
| ৩+ option (elif আছে) | ✅ if/elif/else |
 
---
 
### 04. Logical Operators — and / or / not
 
| Operator | বাংলা | কখন True |
|----------|-------|----------|
| `and` | এবং | দুটো শর্তই True হলে |
| `or` | অথবা | যেকোনো একটি True হলে |
| `not` | না/উল্টো | False → True, True → False |
 
```python
# and — দুটোই লাগবে
if age >= 18 and has_id:
    print("Entry ✅")
 
# or — যেকোনো একটি হলেই চলবে
if is_student or is_senior:
    print("Discount ✅")
 
# not — উল্টো করে
if not is_raining:
    print("Go outside ☀️")
```
 
**Truth Table:**
```
True  AND True  = True   ✅
True  AND False = False  ❌
False OR  True  = True   ✅
False OR  False = False  ❌
not True        = False  ❌
not False       = True   ✅
```
 
---
## append()
Meaning: Add item at the end of list.

```python
fruits = ["Apple"]
fruits.append("Orange")
```

---

## insert()
Meaning: Add item at specific position.

```python
numbers = [1, 3]
numbers.insert(1, 2)
```

---

## remove()
Meaning: Remove specific item.

```python
colors = ["Red", "Blue"]
colors.remove("Blue")
```

---

## pop()
Meaning: Remove item using index.

```python
names = ["Rin", "Sam"]
names.pop(0)
```

---

## del
Meaning: Delete item from list.

```python
numbers = [10, 20, 30]
del numbers[1]
```

---

## extend()
Meaning: Add multiple items.

```python
a = [1, 2]
a.extend([3, 4])
```

---

## count()
Meaning: Count total same values.

```python
numbers = [1, 2, 2]
numbers.count(2)
```

---

## index()
Meaning: Find item position.

```python
fruits = ["Apple", "Banana"]
fruits.index("Banana")
```

---

## sort()
Meaning: Sort low to high.

```python
numbers = [3, 1, 2]
numbers.sort()
```

---

## sort(reverse=True)
Meaning: Sort high to low.

```python
numbers = [3, 1, 2]
numbers.sort(reverse=True)
```

---

## slicing
Meaning: Get specific part of list.

```python
numbers = [10, 20, 30, 40]
print(numbers[1:3])
```

---

## max()
Meaning: Find highest value.

```python
numbers = [5, 8, 2]
max(numbers)
```

---

## min()
Meaning: Find lowest value.

```python
numbers = [5, 8, 2]
min(numbers)
```
### 05. String Methods — লেখা নিয়ে কাজ
 
| Method | কাজ | উদাহরণ | Result |
|--------|-----|---------|--------|
| `len(x)` | কতটি character | `len("Shahid")` | `6` |
| `x.isalpha()` | শুধু অক্ষর কিনা | `"hello".isalpha()` | `True` |
| `x.lower()` | ছোট হাতে | `"YES".lower()` | `"yes"` |
| `x.capitalize()` | প্রথম অক্ষর বড় | `"japan".capitalize()` | `"Japan"` |
| `x.endswith(".com")` | শেষে .com কিনা | `"a@b.com".endswith(".com")` | `True` |
| `x.startswith("260")` | 260 দিয়ে শুরু কিনা | `"2601".startswith("260")` | `True` |
| `"@" in x` | @ আছে কিনা | `"@" in "a@b.com"` | `True` |
| `round(x, 2)` | দশমিক ঠিক করা | `round(4500.001, 2)` | `4500.0` |
 
---
 
### 06. Percentage → Decimal — % হিসাব
 
```
% ÷ 100 = decimal
90% = 0.90 | 10% = 0.10 | 30% = 0.30
```
 
```python
bill = 5000
final = bill * 0.90   # 10% ছাড় → 4500.0
tax   = bill * 0.10   # 10% tax  → 500.0
 
# Homework-এ common uses:
bill   * 0.90   # 10% discount
salary * 0.30   # 30% tax
amount * 0.97   # 3% discount
amount * 0.98   # 2% discount
```
 
---
 
## 🛠️ Part 2 — Developer's Toolkit
 
### 07. File System — ফাইল সিস্টেম
 
**৩টি Core Concept:**
 
1. **File System কী?** — OS যেভাবে disk-এ file store, organize, retrieve করে। Library catalog-এর মতো।
2. **Tree Structure** — উল্টো গাছের মতো। সবার উপরে `Root`। নিচে folder → subfolder → file।
3. **Paths** — প্রতিটি file-এর "ঠিকানা"। Root থেকে destination পর্যন্ত।
**File Tree:**
```
/ (Root)
└── Users/
    └── YourName/
        ├── Documents/
        ├── Downloads/
        └── Projects/          ← তুমি এটা তৈরি করো
            └── my_first_app/
                ├── main.py
                ├── helper.py
                └── README.md
```
 
**Absolute Path — Root থেকে পুরো ঠিকানা:**
```
Windows:   C:\Users\YourName\Projects\main.py
Mac/Linux: /home/yourname/projects/main.py
```
 
**Relative Path — এখন যেখানে আছো সেখান থেকে:**
```
main.py        ← same folder
./main.py      ← explicitly here
../other/f.py  ← go up, then in
```
 
> ⚠️ Python বলে `FileNotFoundError` → প্রায় সবসময় ভুল path! Absolute vs Relative double-check করো।
 
---
 
### 08. Terminal — টার্মিনাল Commands
 
| কাজ | Mac/Linux | Windows CMD | কী করে |
|-----|-----------|-------------|--------|
| কোথায় আছি? | `pwd` | `cd` | current location |
| File list | `ls` | `dir` | সব file/folder |
| Folder-এ ঢোকো | `cd Documents` | `cd Documents` | navigate |
| পিছে যাও | `cd ..` | `cd ..` | এক ধাপ উপরে |
| নতুন folder | `mkdir myapp` | `mkdir myapp` | folder তৈরি |
| নতুন file | `touch main.py` | `type nul > main.py` | file তৈরি |
| VS Code খোলো | `code .` | `code .` | editor open |
| Python চালাও | `python main.py` | `python main.py` | script run |
| ⚠️ Delete file | `rm file.txt` | `del file.txt` | permanent! |
| ⚠️ Delete ALL | `rm -rf folder/` | `rmdir /s /q` | সব মুছে যাবে! |
 
**🚀 Pro Workflow — মুখস্থ করো!**
```
cd Desktop → mkdir new_project → cd new_project → touch main.py → code .
```
 
---
 
### 09. Flowcharts — ফ্লোচার্ট
 
**৪টি Shape:**
 
| Shape | নাম | মানে |
|-------|-----|------|
| ⬭ | Oval / Terminator | START / END — প্রতিটিতে ঠিক একটি |
| ▭ | Rectangle | Process / Action — যেমন: `count = count + 1` |
| ◇ | Diamond | Decision (Yes/No) — if/else-এ map হয় |
| ▱ | Parallelogram | Input / Output — `input()` / `print()` |
 
**Number Guessing Game — Flowchart:**
```
        START
          ↓
   User types a guess
          ↓
   count = count + 1
          ↓
   guess == secret?
    YES ✅    NO ❌
     ↓          ↓
 'Correct!'  Too high/low
     ↓          ↓
    END      ← Loop Back
```
 
**Game Trace — secret = 42:**
 
| Turn | Guess | Result |
|------|-------|--------|
| 1 | 75 | Too high! 🔴 |
| 2 | 20 | Too low! 🔵 |
| 3 | 42 | Correct! ✅ |
 
> 💡 Code লেখার আগে flowchart আঁকো। Bug ধরতেও flowchart সাহায্য করে!
 
---
 
### 10. Algorithms — অ্যালগরিদম
 
**Algorithm কী?**
> Ordered, finite instructions যা একটি নির্দিষ্ট সমস্যা solve করে। শুরু, স্পষ্ট ধাপ ও শেষ থাকতে হবে।
 
**ভালো Algorithm-এর ৫ গুণ:**
- **Correct** — সঠিক উত্তর দেয়
- **Efficient** — দ্রুত কাজ করে
- **Clear** — পড়তে সহজ
- **Finite** — শেষ হয়
- **General** — সব input-এ কাজ করে
**Real World:** Google search · Spotify · GPS routing · Instagram feed
 
**Full Python Code:**
```python
import random
 
secret = random.randint(1, 100)
count  = 0
 
while True:
    guess  = int(input("Guess 1-100: "))
    count += 1
    if guess == secret:
        print(f"Correct! Got it in {count} guesses!")
        break
    elif guess > secret:
        print(f"{guess} too high! Try lower.")
    else:
        print(f"{guess} too low! Try higher.")
```
 
> 🏆 **Golden Rule:** প্রতিটি complex program = simple algorithm-এর সমষ্টি। বড় problem → ছোট ছোট ধাপে ভাগ করো!
 
---
 
## 💼 Part 3 — Software Engineering
 
### 11. SDLC — Software Development Lifecycle
 
> Software কীভাবে plan, create, test ও maintain করা হয় তার structured process।
 
**৭টি Phase (ক্রমানুসারে):**
```
🔍 Planning → 📋 Requirements → 🏛️ Design → 💻 Implementation
→ ✅ Testing → 🚀 Deployment → 🔧 Maintenance
```
 
| Phase | কাজ |
|-------|-----|
| Planning | Scope & feasibility নির্ধারণ |
| Requirements | কী build করবো সেটা define করা |
| Design | Architecture & UX plan করা |
| Implementation | Code লেখা |
| Testing | Verify & validate করা |
| Deployment | Production-এ ship করা |
| Maintenance | Sustain & improve করা |
 
**Waterfall vs Agile vs Scrum vs Kanban:**
 
| Model | Approach | Best For |
|-------|----------|----------|
| **Waterfall** | Linear, no going back | Gov/regulatory projects |
| **Agile** | Iterative, flexible | Modern software products |
| **Scrum** | Agile + defined roles | Cross-functional teams |
| **Kanban** | Visual, continuous | Maintenance & ops |
 
**Scrum Artifacts:**
- **Product Backlog** — সব features-এর prioritized list (Product Owner-এর)
- **Sprint Backlog** — ১-২ সপ্তাহের sprint-এ কী করবো
- **Increment** — Sprint শেষে potentially shippable product
- **Daily Stand-up** — ১৫ মিনিট: কী করলাম? কী করবো? কোনো blocker?
- **Retrospective** — কী ভালো হলো? কী improve করবো?
---
 
### 12. Software Engineering in the AI Era
 
> ⚠️ **Important Shift:** GitHub Copilot, Cursor, Claude — engineers-দের **replace করে না, amplify করে!** AI code তোমাকেই বুঝতে, review করতে ও own করতে হবে।
 
**AI-র ৪টি দিক:**
 
**🤝 AI as Coding Partner**
- Copilot/Cursor: autocomplete & code generation
- Claude/ChatGPT: debugging, explaining, reviewing
- AI boilerplate লেখে, তুমি architect করো
- Prompt করতে শেখো — এটা নতুন skill!
**🧠 LLM-Powered Apps**
- Modern apps language models কে feature হিসেবে integrate করে
- RAG systems: নিজের data থেকে AI answer দেয়
- Streaming APIs, function calling, agentic workflows
- 2025-এ এটা optional নয়!
**👁️ Computer Vision**
- AI "দেখে" — image classification, object detection
- Medical imaging: X-rays, MRIs diagnose করে
- Classical CV ও deep learning-এর সেতু
**⚠️ Risks to Watch**
- AI hallucinations — plausible কিন্তু ভুল code
- Security vulnerabilities in AI-generated code
- Fundamentals না বুঝে over-reliance
- Prompt injection attacks in AI apps
---
 
### 13. Responsibilities of a Software Engineer
 
**৬টি Core Responsibility:**
 
**📋 Requirements Analysis**
- Business needs → technical specs-এ রূপান্তর
- Clients, PMs, stakeholders-এর সাথে যোগাযোগ
- Code লেখার আগে ambiguity চিহ্নিত করা
- Functional & non-functional requirements document করা
**🏛️ System Design & Architecture**
- Problem-এর জন্য সঠিক tech stack বেছে নেওয়া
- Databases, APIs, service boundaries design করা
- Scalability, availability, security-র plan
- ERDs, sequence, class diagrams তৈরি
**💻 Implementation (Coding)**
- Clean, readable, well-documented code লেখা
- Coding standards & conventions follow করা
- Algorithms & data structures implement করা
- Git দিয়ে version control, clear commits
**🧪 Testing & QA**
- Unit, integration, end-to-end tests লেখা
- Debug & resolve defects systematically
- Code reviews-এ participate করা
- Edge cases & failure scenarios validate করা
**🚀 Deployment & DevOps**
- CI/CD pipelines build করা
- Docker দিয়ে applications containerize করা
- AWS, GCP, Azure-এ cloud deploy
- Production monitor, incidents respond
**🔧 Maintenance & Iteration**
- Existing codebase refactor & improve করা
- Bug reports & production issues-এ respond
- Performance bottlenecks optimize করা
- Dependencies upgrade, technical debt handle
> 🌏 **Japan — Bridge SE Perspective:** Japanese client team ও development team-এর মধ্যে communication code-এর মতোই গুরুত্বপূর্ণ। English ও Japanese-এ clearly requirements document করা এই market-এ unique ও valuable skill!
 
---
 
## 📝 Master Summary
 
### Python
- `int/float/str` — input types
- `if/elif/else` — শর্ত
- Ternary — এক লাইনে if/else
- `and/or/not` — logical operators
- `len/isalpha/endswith/startswith` — string methods
- `round(x, 2)` — টাকার হিসাব
- `x * 0.90` — 10% ছাড়
### File System + Terminal
- Tree structure — Root থেকে শাখা
- Absolute path = পুরো ঠিকানা
- Relative path = এখান থেকে
- `pwd/ls` — where/what
- `mkdir/cd` — create/move
- `code .` — VS Code খোলো
- `rm` — সাবধান! permanent delete
### Flowcharts + Algorithms
- ⬭ Oval = START/END
- ▭ Rectangle = Process
- ◇ Diamond = Decision (if/else)
- ▱ Parallelogram = Input/Output
- Code লেখার আগে Flowchart আঁকো!
- Algorithm = ordered steps
- বড় problem → ছোট ছোট ধাপে ভাগ করো
### Software Engineering + AI
- SDLC = 7 phases
- Waterfall / Agile / Scrum / Kanban

 
*Complete Study Notes — Python · Developer's Toolkit · Software Engineering*
