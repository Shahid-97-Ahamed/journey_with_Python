# # class Airplains:
# #     def __init__(self,name,model,capacity,max_speed):
# #         self.name =name
# #         self.model =model
# #         self.capacity =capacity
# #         self.max_speed =max_speed

# # Bg=Airplains("BG616","767",456,215)
# # Jal=Airplains("BG616","767",456,215)
# # dubai=Airplains("BG616","767",456,215)

# # print(Jal.capacity)


# # --------------------------------------------------------------------------

# # class Students:
# #     def __init__(self,name,marks):
# #         self.name =name
# #         self.marks =marks

# #     def get_avg(self):
# #         total =sum(self.marks)
# #         print(f"Hi {self.name},Your avarage markes is {total/len(self.marks):.1f}")

# # my_result=Students("Shahid",[98,85,45,34])
# # my_result.get_avg()


# # ---------------------------------------------------------------------------------

# # Basic Fundamentan python Problems

# # 1.Self Introduction Card

# name ="Shahid"
# age = 32
# city ="Kagoshima"

# # print(f"My name is {name}, I am {age} years old, and I live in {city}.")


# # 2.Suica Card Balance Check

# # balance = int(input("Input your balance: "))
# train_fare = 410

# status ="You can board the train" if balance >= train_fare  else "Insufficient balance"
# # print(status)

# # 3.Train Fare Category

# # age =int(input("Enter Your Age: "))

# # if 0<= age < 12:
# #     # print("Child")
# # elif 12<= age <= 22:
# #     # print("Student")
# # elif 23<= age <=64:
# #     # print("Adult")
# # else:
# #     # print("Senior")

# another way to solve 

# age =int(input("Enter Your Age: "))

# if age in range(0,12):
#     print("Child")
# elif  age in range(12,23):
#     print("Student")
# elif age in range(23,65):
#     print("Adult")
# else:
#     print("Senior")

# # 04.Shinkansen Countdown

# for i in range(10,0,-1):
#         print(i)
# print("Departing Tokyo Station!")

# 05.ATM Withdrawal Attempts

# correct_pin =1234
# attemps = 3

# while attemps > 0:
#     users_pin =int(input("Enter Your pin: "))
#     if users_pin == correct_pin:
#         print("Access granted")
#         break
#     else:
#         attemps = attemps - 1
#         print(f"You have {attemps} attemps left")

# else:
#     print("Card blocked")

# 06. Konbini Shopping List

items = ["onigiri", "tea", "bento"]
items.append("pudding")
items.remove("tea")

for i,item in enumerate(items,1):
    print(f"{i}.{item}")

