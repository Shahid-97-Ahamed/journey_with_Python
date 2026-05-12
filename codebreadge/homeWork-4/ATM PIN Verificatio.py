# 5. ATM PIN Verification
user_pin =int(input("Enter Your Pin Numbers: "))

status ="Access Granted" if user_pin == 1234 else "Access Denied"
print(status)