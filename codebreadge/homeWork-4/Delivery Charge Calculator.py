# 16. Delivery Charge Calculator
cart_amount =int(input("Enter Your Amount: "))
message = "Free Delivery" if cart_amount > 5000 else "Delivery Charge: 500 yen"
print(message)