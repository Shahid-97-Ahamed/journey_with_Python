bookings = []
while True:
    tickets =int(input("Enter number of tickets (o to stop): "))
    if tickets == 0:
        break
    bookings.append(tickets*150)

total_revenue = 0
highest_booking = 0
index = 0

while index < len(bookings):
    amount =bookings[index]
    total_revenue = total_revenue + amount
    if amount > highest_booking:
        highest_booking = amount
    index = index +1

print("Total revenue: ￥",total_revenue)
print("Highest booking amount: ￥",highest_booking)