membership_status =input("Do You have a membership card(yes/no): ").lower()
cart_amount =int(input("Enter Your Cart Amount: "))
if membership_status == "yes" and cart_amount >= 20000:
   bill = cart_amount *0.97
elif membership_status == "yes" and cart_amount >= 10000:
   bill = cart_amount *0.98
elif membership_status == "yes" and cart_amount < 10000:
   bill = cart_amount *0.99
else:
  bill =  cart_amount
print("Final Bill: ",bill)
