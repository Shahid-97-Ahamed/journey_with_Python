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

queue=[]
while True:
    type=input ("Enter (add/emergency/next/quit): ")
    if type =="add":
        patient = input("P_Name:")
        queue.append(patient)
        print("Queue", queue)
    elif type =="emergency":
        patient=input("P_Name:")
        queue.insert(0,patient)
        print("Queue:", queue)
    elif type =="next":
        if len(queue)>0:
            patient=queue.pop(0)
            print("Calling: ",patient)
            print("Queue: ", queue)
        else:
            print("No patiaent waiting.")
    elif type =="quit":
        print ("Exit")
        break
    else:
        print("Type Invalid")



