# 13. . Login System with Nested Conditions
users_name =input("Enter Your Name: ")
users_password =input("Enter Your Password: ")
if users_name == "admin" and users_password == "12345":
    print("Login Successful")
elif users_name != "admin":
    print("Invalid Username")
else : 
    print("Wrong Password")
