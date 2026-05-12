# 6. Electricity Bill Warning
unit =int(input("Enter Your Unit: "))

status ="High Bill" if unit > 500 else "Normal Bill"
print(status)