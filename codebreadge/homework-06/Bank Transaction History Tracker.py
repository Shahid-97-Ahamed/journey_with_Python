balance = 100000

transaction_types = []
transaction_amounts = []

deposit_count = 0
withdraw_count = 0

print("Opening Balance:", balance)

while True:
    transaction_type = input(
        "Enter transaction type (deposit/withdraw or 'done'): "
    ).lower()

    if transaction_type == "done":
        break

    amount = int(input("Enter amount: "))

    # Withdraw validation
    if transaction_type == "withdraw" and amount > balance:
        print("Rejected: Insufficient balance")
        continue

    # Store data
    transaction_types.append(transaction_type.upper())
    transaction_amounts.append(amount)

    # Update balance
    if transaction_type == "deposit":
        balance += amount
        deposit_count += 1

    elif transaction_type == "withdraw":
        balance -= amount
        withdraw_count += 1

print("=" * 44)
print("TRANSACTION HISTORY")
print("=" * 44)
print("No. | Type | Amount | Balance")
print("-" * 44)

running_balance = 100000
index = 0

while index < len(transaction_types):

    current_type = transaction_types[index]
    current_amount = transaction_amounts[index]

    if current_type == "DEPOSIT":
        running_balance += current_amount
        amount_display = "+" + str(current_amount)

    else:
        running_balance -= current_amount
        amount_display = "-" + str(current_amount)

    print(
        index + 1,
        "|",
        current_type,
        "|",
        amount_display,
        "|",
        running_balance
    )

    index += 1

print("-" * 44)
print("Total Transactions :", len(transaction_types))
print("Total Deposits :", deposit_count)
print("Total Withdrawals :", withdraw_count)
print("Closing Balance :", balance)