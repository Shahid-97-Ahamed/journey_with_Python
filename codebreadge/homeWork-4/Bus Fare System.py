# 11. Bus Fare System
passengers_age =int(input("Enter Your Age: "))
if passengers_age <= 12:
    print("Bus fare: 150 yen")
elif passengers_age <= 17:
    print("Bus fare: 300 yen")
elif passengers_age <= 59:
    print("Bus fare: 500 yen")
else :
    print("Bus fare: 200 yen")
