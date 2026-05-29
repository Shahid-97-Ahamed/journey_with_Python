# print('Allah')
# print ("Bismillah")
# scrite_number = 7

# while True:
#     guess_number = int(input("Enter your number: "))

#     if scrite_number == guess_number:
#         print("Congratulation")
#         break
#     else:
#         print("Try again!!")

# secret_password = "python123"
# while True:
#     users =input("Enter Your Password: ")
#     if secret_password == users:
#         print("Access Granted")
#         break
#     else:
#         print("Wrong Password, Try Again!")

# secret_pin = 4321
# attemps = 0

# while attemps < 3:
#     users_pass =int(input("Enter your password: "))
#     if secret_pin == users_pass:
#         print("Login Successful")
#         break
#     else:
#         print("Wrong PIN")
#         attemps +=1
#         if attemps > 2:
#             print("ATM Card Blocked")

number = 15
attemps = 0
while attemps < 5:
    guess_number =int(input("Guess The Number: "))
    if number == guess_number:
        print("You Win!")
        break
    elif guess_number > number:
        print("Too High!")  
    else:
        print("Too Low!")
        attemps += 1
        remining =5 - attemps
        print("remaining attempts: ",remining)
        if attemps == 5:
            print("GAME OVER")

        
       
       
            