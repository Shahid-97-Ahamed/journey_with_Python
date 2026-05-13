# 22. Smart Login Security System
username =input("Enter Your Username: ")
user_password =input("Enter Your Password: ")
user_otp =input("Enter Your OTP: ")
if username == "admin" and user_password == "12345" and user_otp == "9999":
    print("Login Approved")
elif username != "admin":
    print("Invalid Username")
elif user_password != "12345":
    print("Wrong Password")
else: 
    print("Invalid OTP")