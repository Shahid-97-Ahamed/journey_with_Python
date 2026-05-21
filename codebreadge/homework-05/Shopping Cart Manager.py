# Shopping Cart Manager

#Start with an empty list
cart = []

#take input for 3 times
items1 = input("Enter Your Items 1: ").capitalize()
cart.append(items1)
items2 = input("Enter Your Items 2: ").capitalize()
cart.append(items2)
items3 = input("Enter Your Items 3: ").capitalize()
cart.append(items3)

# print cart
print("Your cart: ",cart)

# Print Your number of items
print("Total items:",len(cart))