# 4. Warehouse Stock Manager


inventory = []

while True:

    name = input("Enter product name (or 'done'): ")

    if name.lower() == "done":
        break

    category = input("Enter category: ")

    qty = int(input("Enter quantity: "))

    price = float(input("Enter unit price: "))

    inventory.append([
        name.title(),
        category.upper(),
        qty,
        price
    ])

highest_value = 0
highest_product = ""

print("=" * 60)
print("WAREHOUSE INVENTORY REPORT")
print("=" * 60)

print("Product | Category | Qty | Unit Price | Total Value | Stock")
print("-" * 60)

i = 0

while i < len(inventory):

    name = inventory[i][0]
    category = inventory[i][1]
    qty = inventory[i][2]
    price = inventory[i][3]

    total_value = qty * price

    if qty >= 100:
        stock = "High"

    elif qty >= 50:
        stock = "Medium"

    else:
        stock = "Low"

    print(
        name, "|",
        category, "|",
        qty, "|",
        price, "|",
        total_value, "|",
        stock
    )

    if total_value > highest_value:
        highest_value = total_value
        highest_product = name

    i += 1

print("-" * 60)
print(
    "Highest value product:",
    highest_product,
    "(" + str(highest_value) + " yen)"
)