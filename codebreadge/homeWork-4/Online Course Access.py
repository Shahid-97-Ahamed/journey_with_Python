# 8. Online Course Access
user_age =int(input("Enter Your Age: "))
country =input("Enter Your Country Name: ").capitalize()

status = "Access Granted" if user_age >= 18 or country == "Japan" else "Access Denied"
print(status)