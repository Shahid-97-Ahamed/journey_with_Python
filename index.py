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


