# 5. ATM PIN Verification
correct_pin = 1234
user_pin =int(input("Enter Your Pin Numbers: "))

status ="Access Granted" if user_pin == correct_pin else "Access Denied"
print(status)