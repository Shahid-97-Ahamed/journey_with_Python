# # # # # # # # # # # # First Program
# # # # # # # # # # # # print("Hello, World!")
# # # # # # # # # # # # print("I am a Python programmer now 🎉")

# # # # # # # # # # # # Comments

# # # # # # # # # # # name       = "Alice"    # string
# # # # # # # # # # # age        = 25         # integer
# # # # # # # # # # # height     = 5.6        # float
# # # # # # # # # # # is_student = True      # boolean
# # # # # # # # # # # nothing    = None      # null value


# # # # # # # # # # # # Multiple assignment
# # # # # # # # # # # x, y, z = 1, 2, 3

# # # # # # # # # # # # Same value to multiple vars
# # # # # # # # # # # a = b = c = 0

# # # # # # # # # # # # print(name,age,height)

# # # # # # # # # # # x = 42
# # # # # # # # # # # # print(type(x))  
# # # # # # # # # # # # print(isinstance(x, int))  

# # # # # # # # # # # # b2  = bool(21245) 
# # # # # # # # # # # # print(b2)

# # # # # # # # # # # # lis =list("abc")
# # # # # # # # # # # # print(lis)

# # # # # # # # # # # x =10
# # # # # # # # # # # x = x/4
# # # # # # # # # # # # print(x)

# # # # # # # # # # # # print("Ha" * 3)             # HaHaHa
# # # # # # # # # # # # print("Hello" + " World")   # Hello World

# # # # # # # # # # # # String Indexing & Slicing
# # # # # # # # # # # # s = "Python"
# # # # # # # # # # # #    P  y  t  h  o  n
# # # # # # # # # # # #    0  1  2  3  4  5   forward
# # # # # # # # # # # #   -6 -5 -4 -3 -2 -1   backward
# # # # # # # # # # # # print(s[0])      # P      first char
# # # # # # # # # # # # print(s[-1])     # n      last char
# # # # # # # # # # # # print(s[1:4])    # yth    index 1,2,3
# # # # # # # # # # # # print(s[:3])     # Pyt    start to 2
# # # # # # # # # # # # print(s[3:])     # hon    3 to end
# # # # # # # # # # # # print(s[::-1])   # nohtyP reversed!


# # # # # # # # # # s = "   Hello World"
# # # # # # # # # # print(s.endswith(" "))

# # # # # # # # # name, age = "Ravi", 21

# # # # # # # # # # # % formatting (old)
# # # # # # # # # # print("Name: %s, Age: %d" % (name, age))

# # # # # # # # # # .format()
# # # # # # # # # print("Name: {}, Age: {}".format(name, age))

# # # # # # # # price = float(input("Enter price: ₹"))
# # # # # # # # print(f"With 18% GST: ₹{price*1.18:.2f}")

# # # # # # # print("Hello",end="")
# # # # # # # print("hshjkhfjsdjfjsjdjfsd,mvndbvhksdhfkvsdhjfvjsdjjfgvlisej")
# # # # # # # print("gfdhfhb",end="")
# # # # # # # print("3636936")

# # # # # # # print("Line1\nLine2")
# # # # # # # print("Tab:\there") 
# # # # # # # print("She said \"hi\"")  

# # # # # # # Project Calculator

# # # # # # a =float(input("first number: "))
# # # # # # op =input("Operation(+,-,*,/): ")
# # # # # # b =float(input("second number: "))


# # # # # # if op =="+":
# # # # # #     print(f"Result:{a+b}")
# # # # # # elif op =="-":
# # # # # #     print(f"Result:{a-b}")
# # # # # # elif op == "*":
# # # # # #     print(f"Result:{a*b}")
# # # # # # elif op =="/":
# # # # # #     if b !=0:
# # # # # #         print(f"Result:{a/b:.2f}")
# # # # # #     else:
# # # # # #         print("Error: Cannot divide by zero!")
# # # # # # else:
# # # # # #     print("Invalid Oparator")

# # # # # # day = "Monday"

# # # # # # match day:
# # # # # #     case "Monday" | "Tuesday":
# # # # # #         print("Start of week")
# # # # # #     case "Friday":
# # # # # #         print("Almost weekend!")
# # # # # #     case "Saturday" | "Sunday":
# # # # # #         print("Weekend! 🎉")
# # # # # #     case _:
# # # # # #         print("Midweek")


# # # # # fruits = ["apple", "mango", "banana"]
# # # # # for fruit in fruits:
# # # # #     print(f"I like {fruit}")

# # # # # for i in range(3):
# # # # #     pass
# # # # # for i in range(1, 4):
# # # # #     for j in range(1, 4):
# # # # #         print(f"{i}x{j}={i*j}", end="  ")
# # # # #     print()

# # # # # def profile(**info):
# # # # #     for k, v in info.items():
# # # # #         print(f"{k}: {v}")

# # # # # profile(name="Ravi", age=21, city="Delhi")


# # # # # def fib(n):
# # # # #     if n <= 1: return n
# # # # #     return fib(n-1) + fib(n-2)

# # # # # print([fib(i) for i in range(8)])

# # # # lst = [3, 1, 4, 1, 5]
# # # # # lst.insert(0, 99)
# # # # # lst.extend([7,8])
# # # # # lst.remove(1)
# # # # # lst.pop() 
# # # # # lst.sort() 
# # # # # lst.sort(reverse=True) 
# # # # # lst.reverse() 
# # # # # print(lst)
# # # # # print(lst.index(4))
# # # # # print(lst.count(1)) 
# # # # # copy = lst.copy()

# # # # # lst.clear()    
# # # # # print(lst)

# # # # nums = [5, 3, 8, 1, 9]
# # # # # print(len(nums))           # 5  → length
# # # # # print(sum(nums))           # 26 → total
# # # # # print(min(nums))           # 1  → smallest
# # # # # print(max(nums))           # 9  → largest
# # # # # print(sorted(nums))        # [1,3,5,8,9] new list!
# # # # # print(list(reversed(nums))) # reversed new list
# # # # # print(3 in nums)            # True


# # # # # A = {1,2,3}
# # # # # # A.add(4) 
# # # # # # A.discard(2)  
# # # # # A.remove(3)   
# # # # # print(A)


# # # # person = {
# # # #     "name": "Alice",
# # # #     "age":  25,
# # # #     "city": "Delhi"
# # # # }

# # # # # print(person["name"])
# # # # # print(person.get("age"))
# # # # # print(person.get("email","N/A"))

# # # # d = {"a":1, "b":2, "c":3}

# # # # # print(d.keys())  
# # # # # print(d.items())
# # # # # d.update({"d":4, "e":5})
# # # # # d.pop("a")  
# # # # # d.setdefault("z", 99)
# # # # # # print(d)
# # # # # print(len(d))

# # # # # for key, val in d.items():
# # # # #     print(f"{key} → {val}")

# # # # # Dict comprehension: {key: value for item in iterable}
# # # # squares = {x: x**2 for x in range(1,6)}
# # # # # {1:1, 2:4, 3:9, 4:16, 5:25}

# # # # # Real example: Word frequency counter
# # # # text = "apple banana apple cherry banana apple"
# # # # freq = {}
# # # # for word in text.split():
# # # #     freq[word] = freq.get(word, 0) + 1

# # # # # print(freq)

# # # # unique_mod = {x%3 for x in range(10)}
# # # # # print(unique_mod)

# # # # gen = (x**2 for x in range(1000000))  # only stores formula
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))
# # # # # print(next(gen))

# # # # total = sum(x**2 for x in range(1000000))
# # # # # print(total)


# # # # # try:
# # # # #     x = int(input("Enter a number: "))
# # # # #     print(100 / x)
# # # # # except ValueError:
# # # # #     print("Not a valid number!")
# # # # # except ZeroDivisionError:
# # # # #     print("Cannot divide by zero!")
# # # # # except Exception as e:
# # # # #     print(f"Unexpected error: {e}")
# # # # # else:
# # # # #     print("No errors! Everything went well ✅")  # runs if NO error
# # # # # finally:
# # # #     # print("This ALWAYS runs — cleanup code here")

# # # # # def set_age(age):
# # # # #     if not isinstance(age, int):
# # # # #         raise TypeError("Age must be an integer")
# # # # #     if age < 0 or age > 150:
# # # # #         raise ValueError(f"Invalid age: {age}")
# # # # #     return age

# # # # # try:
# # # # #     set_age(-5)
# # # # # except ValueError as e:
# # # # #     print(e)   # Invalid age: -5

# # # # with open("notes.txt", "w") as f:
# # # #     f.write("Hello, File!\n")
# # # #     f.write("Second line\n")

# # # # Read entire file as one string
# # # with open("notes.txt", "r") as f:
# # #     content = f.read()
# # #     print(content)

# # # Read line by line (memory efficient)
# # with open("notes.txt") as f:
# #     for line in f:
# #         print(line.strip())      # strip removes \n
# # Read all lines into a list
# # with open("notes.txt") as f:
#     # lines = f.readlines()
     
# import json

# data = {"name": "Alice", "scores": [90, 85, 92], "active": True}

# # # Write to JSON file
# # with open("data.json", "w") as f:
# #     json.dump(data, f, indent=4)   # indent makes it pretty
# # Read from JSON file
# with open("data.json") as f:
#     loaded = json.load(f)
# print(loaded["name"])             # Alice

import csv

# # Write CSV
# with open("students.csv", "w", newline="") as f:
#     w = csv.writer(f)
#     w.writerow(["Name", "Score"])
#     w.writerow(["Alice", 90])
#     w.writerow(["Bob", 85])

# Read CSV
with open("students.csv") as f:
    reader = csv.DictReader(f)   # header as keys
    for row in reader:
        print(row["Name"], row["Score"])