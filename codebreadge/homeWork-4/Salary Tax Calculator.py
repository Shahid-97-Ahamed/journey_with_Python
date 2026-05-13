# 18. Salary Tax Calculator
salary = int(input("Enter Your Salary: "))
if salary > 1000000:
   tax =salary * 0.30
elif salary > 500000:
    tax = salary * 0.10
else:
   tax = 0
print("Tax: ",tax)
