member_count = 0
total_revenue = 0

while True:

    name = input("Enter member name (or 'stop' to exit): ")

    if name.lower() == "stop":
        break

    age = int(input("Enter age: "))
    plan = input("Enter plan (basic/premium/vip): ").lower()

    # Plan fee selection
    if plan == "basic":
        fee = 2000

    elif plan == "premium":
        fee = 4000

    elif plan == "vip":
        fee = 7000

    else:
        print("Invalid plan!")
        continue

    # Discount calculation
    if age >= 60:
        discount = 20
        payable = fee * 0.80

    elif age <= 15:
        discount = 30
        payable = fee * 0.70

    else:
        discount = 0
        payable = fee

    print(
        f"{name} -> Plan: {plan} | Fee: {fee} | "
        f"Discount: {discount}% | Payable: {payable}"
    )

    member_count += 1
    total_revenue += payable

print("\nTotal members:", member_count)
print("Total revenue:", total_revenue)