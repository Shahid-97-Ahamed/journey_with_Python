# 3. Restaurant Membership Discount
membership_status =input("Yau have a membership (type yes or no): ").lower()
bill =int(input("Enter Your Amount: "))

status = bill * 0.90 if membership_status == "yes" else bill
print("Final bill:",round(status))