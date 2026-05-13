# 17. Website Age Restriction
users_age = int(input("Enter Your Age: "))
message = "Account creation allowed" if users_age >= 13 else "Account creation denied"
print(message)