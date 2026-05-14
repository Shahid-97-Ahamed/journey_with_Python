# 26. Flight Ticket System
nationality =input("Please Input Your Country: ").capitalize()
passport_validity =input("Do You Have Valid Passport(yes/no): ").lower()
status = "Ticket Booking Allowed" if passport_validity == "yes" else "Ticket Booking Denied"
print(status)