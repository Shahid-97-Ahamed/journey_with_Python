products = []
prices = []

while True:

    name = input("Enter product (or 'done' to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter price: "))

    products.append(name)
    prices.append(price)

print("\n--- Your Receipt ---")

index = 0

while index < len(products):
    print(products[index], ":", prices[index])
    index += 1

print("Total items:", len(products))
print("Total bill:", sum(prices))