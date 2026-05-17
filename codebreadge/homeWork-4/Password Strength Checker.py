# 7. Password Strength Checker

users_password =input("Enter Your Password: ")

if not users_password.isalpha() and not users_password.isdigit() and len(users_password)>=8:
    print("Strong Password")
else:
    print("Weak Password")