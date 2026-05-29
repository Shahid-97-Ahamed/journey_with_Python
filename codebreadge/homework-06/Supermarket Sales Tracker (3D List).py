branch_names = ["Shibuya", "Shinjuku"]
category_names = ["Food", "Drinks", "Snacks"]

sales = [
    [  # Shibuya
        [120000, 135000, 118000, 142000],  # Food
        [85000, 90000, 88000, 95000],      # Drinks
        [45000, 50000, 47000, 53000]       # Snacks
    ],

    [  # Shinjuku
        [155000, 160000, 148000, 170000],  # Food
        [92000, 98000, 94000, 102000],     # Drinks
        [60000, 65000, 58000, 70000]       # Snacks
    ]
]

print("=" * 40)
print("SUPERMARKET SALES REPORT")
print("=" * 40)

highest_sale = 0
highest_branch = ""
highest_category = ""
highest_week = 0

b = 0

while b < len(sales):

    print("\nBranch:", branch_names[b])

    branch_total = 0

    c = 0

    while c < len(sales[b]):

        print(category_names[c], "|", end=" ")

        w = 0

        while w < len(sales[b][c]):

            current_sale = sales[b][c][w]

            print(
                f"Week {w+1}: {current_sale}",
                end=" "
            )

            branch_total += current_sale

            if current_sale > highest_sale:
                highest_sale = current_sale
                highest_branch = branch_names[b]
                highest_category = category_names[c]
                highest_week = w + 1

            w += 1

        print()
        c += 1

    print("Branch Total:", branch_total)

    b += 1

print("\nHighest single-week sale:", highest_sale)
print(
    "Branch:",
    highest_branch,
    "| Category:",
    highest_category,
    "| Week",
    highest_week
)