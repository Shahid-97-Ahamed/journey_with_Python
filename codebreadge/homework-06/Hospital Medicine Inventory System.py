medicine_names = []
quantities = []
unit_prices = []

while True:
    name = input("Enter medicine name (or 'done'): ")

    if name.lower() == "done":
        break

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    medicine_names.append(name.title())
    quantities.append(quantity)
    unit_prices.append(price)

print("\n" + "=" * 58)
print("PHARMACY INVENTORY REPORT")
print("=" * 58)
print("Medicine | Qty | Unit Price | Total Value | Status")
print("-" * 58)

index = 0

highest_value = 0
highest_medicine = ""

while index < len(medicine_names):

    total_value = quantities[index] * unit_prices[index]

    if quantities[index] >= 100:
        status = "Sufficient"
    elif quantities[index] >= 50:
        status = "Low"
    else:
        status = "Critical"

    print(
        medicine_names[index], "|",
        quantities[index], "|",
        unit_prices[index], "|",
        total_value, "|",
        status
    )

    if total_value > highest_value:
        highest_value = total_value
        highest_medicine = medicine_names[index]

    index += 1

print("-" * 58)
print(f"Highest value stock: {highest_medicine} ({highest_value} yen)")