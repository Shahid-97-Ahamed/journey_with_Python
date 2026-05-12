# 4. Username Validator
user_name =input("Enter Your Name: ")
# user_name = user_name.isalpha()

massage = "Valid username" if user_name.isalpha and len(user_name) >= 5 else "Invalid User"
print(massage)