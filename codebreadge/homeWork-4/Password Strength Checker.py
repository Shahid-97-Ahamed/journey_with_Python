# 7. Password Strength Checker

users_password =input("Enter Your Password: ")

has_digit =("0" in users_password or
"1" in users_password or
"2" in users_password or
"3" in users_password or
"4" in users_password or
"5" in users_password or
"6" in users_password or
"7" in users_password or
"8" in users_password or
"9" in users_password)

massege ="Strong Password" if len(users_password) >= 8 and has_digit else "Weak Password"
print(massege)