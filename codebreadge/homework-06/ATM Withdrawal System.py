balance = 50000

print("Balance:", balance)

while True:

    amount = int(input("Enter withdrawal amount (0 to exit): "))

    if amount == 0:
        break

    elif amount > balance:
        print("Insufficient funds.")

    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)

print("Thank you! Final balance:", balance)