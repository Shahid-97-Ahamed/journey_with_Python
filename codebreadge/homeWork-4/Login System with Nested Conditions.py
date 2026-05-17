# 13. . Login System with Nested Conditions
password = "12345"
name = "admin"
users_name =input("Enter Your Name: ")
users_password =input("Enter Your Password: ")
if users_name == name and users_password == password:
    print("Login Successful")
elif users_name != "admin":
    print("Invalid Username")
else : 
    print("Wrong Password")
