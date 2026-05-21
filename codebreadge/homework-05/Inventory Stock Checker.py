# 10. Inventory Stock Checker

products = [0, 5, 12, 0, 3]

# total products count
total_stock = len(products)

# max and min stock
max_stock_quantity = max(products)
min_stock_quantity = min(products)

# update first 0 quantity item
products[0] = 8

# output
print("Total products:", total_stock)
print("Max stock:", max_stock_quantity, "| Min stock:", min_stock_quantity)
print("Updated stock:", products)