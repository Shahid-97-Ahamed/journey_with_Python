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

# class Students:
#     def __init__(self,name,marks):
#         self.name =name
#         self.marks =marks

#     def get_avg(self):
#         total =sum(self.marks)
#         print(f"Hi {self.name},Your avarage markes is {total/len(self.marks):.1f}")

# my_result=Students("Shahid",[98,85,45,34])
# my_result.get_avg()


# ---------------------------------------------------------------------------------

# Basic Fundamentan python Problems

# 1.Self Introduction Card

# name ="Shahid"
# age = 32
# city ="Kagoshima"

# print(f"My name is {name}, I am {age} years old, and I live in {city}.")


# 2.Suica Card Balance Check

balance = int(input("Input your balance: "))
train_fare = 410

status ="You can board the train" if balance >= train_fare  else "Insufficient balance"
print(status)