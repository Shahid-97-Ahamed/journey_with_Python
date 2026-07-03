# ----------------------------------Python Zero To Advance------------------------------------

# name = "Rahim"
# age = 20
# hobbie = "Playing Football"
# print("My Name is: ",name)
# print("My age is: ",age)
# print("My hobbie is: ",hobbie)


#------------------------ Input---------------------------

# users_name=input("Enter Your name: ")
# users_birthYear=int(input("Enter Your Birth Year: "))
# present_years = 2026
# age =present_years - users_birthYear
# print(f"Hello {users_name}! Your age is {age}")

# -------------------If-else condition-----------------------------

# digits = int(input("Input Your degits: "))
# if digits % 2 == 1:
#     print(f"{digits} is an Odd number")
# else:
#     print(f"This {digits} is Even number")

# students_exam_number =int(input("Enter the Number: "))

# if students_exam_number >= 80:
#     print("Your grade is: A+")
# elif students_exam_number >= 70:
#     print("Your grade is: A")
# elif students_exam_number >= 60:
#     print("Your grade is: B")
# elif students_exam_number >= 50:
#     print("Your grade is: C")
# else:
#     print("Fail")


# -------------------------for-loop and range---------------------------------

# for i in range(1,1001):
#     print(i)

# num =int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{num} * {i} = {num * i}")

# -------------------------Accumulator( যোগফল জমানো প্যাটার্ন) ----------------

# total = 0
# for i in range (1,6):
#     total += i
# print(total)

# N =int(input("Enter a number: "))

# total = 0
# for i in range(1,N+1):
#     if i % 2 == 0:
#         total = total + i
# print(f"Sum of even numbers from 1 to {N} is: {total}")


# ----------------------while loop---------------------------------------

# for লুপ ব্যবহার হয় যখন জানো কতবার ঘুরতে হবে। 
# কিন্তু যদি না জানো কতবার লাগবে — শুধু জানো কোন শর্তে থামতে হবে? তখন while

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# pin = 1234
# count = 1
# while True:
#     users_pin =int(input("Enter Your Pin: "))
#     if  users_pin == pin:
#         print("Welcome!")
#         break
#     else:
#         print("Try again")
#         count += 1


# ----------------------------------------------------------

# -------------------------------------List--------------------------------

# numbers = [10, 25, 8, 42, 16]    # বর্গ বন্ধনীতে, কমা দিয়ে আলাদা

# for num in numbers:
#     print(num)      
# len(numbers)   # প্রতিটা সংখ্যা একে একে আসবে


# numbers = [12, 45, 7, 89, 23, 56]
# largest = numbers[0]          # ধরে নিলাম প্রথমটাই সবচেয়ে বড়

# for num in numbers:
#     if num > largest:             # এই সংখ্যা কি এখনকার largest এর চেয়ে বড়?
#         largest =num      # হ্যাঁ হলে, একেই largest বানাও

# print(f"The largest number is: {largest}")    # print লুপের বাইরে!

# queue=[]
# while True:
#     type=input ("Enter (add/emergency/next/quit): ")
#     if type =="add":
#         patient = input("P_Name:")
#         queue.append(patient)
#         print("Queue", queue)
#     elif type =="emergency":
#         patient=input("P_Name:")
#         queue.insert(0,patient)
#         print("Queue:", queue)
#     elif type =="next":
#         if len(queue)>0:
#             patient=queue.pop(0)
#             print("Calling: ",patient)
#             print("Queue: ", queue)
#         else:
#             print("No patiaent waiting.")
#     elif type =="quit":
#         print ("Exit")
#         break
#     else:
#         print("Type Invalid")

name ="Ahamed Shahid"
# print(name.find("A"))
# print(name.replace("Aha","Rabbi"))

# print(5//2)
# print(5252%2252)
# print(10**5)

votes =["Abdul","Babor","Abdulla","Abdul"]
# Square brackets [ ] create a list
cart = ["milk", "bread", "eggs", "milk"]  # duplicates OK!
# print(cart)
# print(len(cart))  # 4

fruits = ["apple", "banana", "cherry", "mango"]
# print(fruits[0])    # "apple"  ← first
# print(fruits[-1])   # "mango"  ← last
# print(fruits[1:3])  # ["banana","cherry"] ← slice

# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "orange"  # replace banana
# print(fruits)  # ["apple", "orange", "cherry"]

# fruits = ["apple", "banana"]

# fruits.append("cherry")    # add to END — most common
# print(fruits)  # ["apple","banana","cherry"]

# fruits.insert(1, "mango")   # add at position 1
# print(fruits)  # ["apple","mango","banana","cherry"]

# more = ["grape", "kiwi"]
# fruits.extend(more)           # add ALL items from another list

fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")  # removes FIRST match
fruits.pop(0)             # removes by index, returns it
del fruits[0]             # delete by index
fruits.clear()            # wipe everything → []

students = ["Alice", "Bob", "Carol"]

# for student in students:
#     print(f"Hello, {student}!")

# # With index number
# for i, student in enumerate(students):
#     print(f"{i+1}. {student}")  # 1. Alice  2. Bob  3. Carol

# Old way (3 lines)
# squares = []
# for x in range(1, 6):
#     squares.append(x**2)

# # List comprehension (1 line!)
# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]

# # With a filter — only even numbers
# evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens)    # [2, 4, 6, 8, 10]

# # Transform — uppercase all names
# names = ["alice", "bob"]
# upper = [n.upper() for n in names]  # ["ALICE","BOB"]

# **********************Arrange items in alphabetical or numerical order********************
nums =[3, 1, 4, 1, 5, 9]
fruits =["banana", "apple", "cherry"]

nums.sort()# sorts IN PLACE → [1,1,3,4,5,9]
# print(nums)
nums.sort(reverse=True)# descending → [9,5,4,3,1,1]
# print(nums)

#  sorted() keeps original unchanged, returns new list

result =sorted(fruits)
# print(result)# ["apple","banana","cherry"]
# print(fruits)# ["banana","apple","cherry"] ← unchanged!

scores =[1,2,1,2,5,1,5,2,6,1,5,8]
scores.sort(reverse=True)
# print(f"The winner is {scores[0]}")

# *******************************Tuples******************************************

# A tuple is like a list that can never be changed
# Once created, items are locked in — you can't add, remove, or change them. This is called being immutable. It sounds limiting, but it's actually a feature that protects important data.
# Real life: Birth certificate

location =(35.675,139.565)
# color=(255,165,0)
# print(type(location))

# Access by index — exactly like a list
# print(color[0])
# print(color[-1])
# print(color[:-1])

# if 139.565 in location:
    # print("Its Tokyo")

# Assign each value to its own variable in one line

color =(255,520,1259)
red,black,green=color
# print(red,black,green)

coords =(35.6762,139.6503)
# coords[0]=0
# print(coords)# ❌ TypeError: 'tuple' object does not support item assignment

city_map ={(35.68,139.69):"Tokyo",(48.54,2.35):"Paris"}
# print(city_map[(48.54,2.35)])

# ********************************Sets*******************************************

# Unique items only, unordered. Built for speed and maths-style operations.

# Real life: Ballot box

# Curly braces { } with values = set
colours ={"red","blue","green"}

# Duplicates removed automatically!
tags = {"python", "coding", "python", "tutorial", "coding"}
# print(tags)  # {'python', 'coding', 'tutorial'} — 3 unique items

# Convert a list → set to deduplicate instantly
votes =["Alice","Bob","Alice","Carol","Bob"]
unique =set(votes)
# print(unique)


fruits ={"apple","banana"}

fruits.add("cherry")
# print(fruits)

fruits.update(["mango","grape"])
# print(fruits)

fruits.remove("banana")
# print(fruits)

fruits.discard("pineapple")
# print(fruits)

# if "apple" in fruits:
#     print("Found it!")

A ={1,2,3,4,5}
B={4,5,6,7,8}

# print(A | B)# Union — ALL unique items from both   → {1,2,3,4,5,6,7,8}
# print(A & B)# Intersection — ONLY in BOTH          → {4, 5}
# print(A - B)# Difference — in A but NOT in B       → {1, 2, 3}
# print(A ^ B)# Symmetric diff — in one but not both → {1,2,3,6,7,8}

A = {1, 2, 3, 4}
B = {1, 2}

# print(A.issuperset(B))

A = {1, 2}
B = {3, 4}

# print(A.isdisjoint(B))

fruits = {"apple", "banana", "orange"}

fruits.clear()

# print(fruits)

# ****************************************Python Dictionaries******************************

# A dictionary maps a key to a value — like a real dictionary
# Real life: A real dictionary


student ={
    "name":"Shahid",
    "age":22,
    "grade":"A",
    "passed":True
}

# print(student)
# print(len(student))

student ={"name":"Aiko","age":22}

# print(student["name"])
# print(student.get("score","N/A"))


key =student.keys()
value=student.values()
item=student.items()
# print(key)
# print(value)
# print(item)

student["grade"]="C"

student["age"]=55
# print(student)

student.update({"city": "Tokyo", "grade": "A+"})
# print(student)

# Four ways to delete entries

student ={"name": "Aiko", "age": 22, "grade": "A"}

# removed =student.pop("grade")
# # print(student)
# del student["age"]
# print(student)
# student.popitem()
# print(student)
# student.clear()
# print(student)

# Loop over keys, values, or both at the same time

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(value)

# for key, value in student.items():
#     print(f"{key}:{value}")

school = {
    "s1": {"name": "Alice", "grade": "A"},
    "s2": {"name": "Bob",   "grade": "B"},
}

# print(school["s1"]["name"])

# for sid, info in school.items():
#     print(f"{info["name"]} got {info["grade"]}")