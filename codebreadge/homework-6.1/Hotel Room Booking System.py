# 2. Hotel Room Booking System

rooms = [
    ["Standard", 5000, 1],
    ["Deluxe", 8000, 1],
    ["Suite", 15000, 1],
    ["Family", 10000, 1],
    ["Executive", 20000, 1]
]

booked_count = 0
revenue = 0

print("=" * 40)
print("HOTEL ROOM AVAILABILITY")
print("=" * 40)

print("No. | Type | Price/Night | Status")
print("-" * 40)

i = 0

while i < len(rooms):

    status = "Available" if rooms[i][2] == 1 else "Booked"

    print(
        i + 1,
        "|",
        rooms[i][0],
        "|",
        rooms[i][1],
        "|",
        status
    )

    i += 1


while True:

    room_no = int(input("\nEnter room number to book (0 to exit): "))

    if room_no == 0:
        break

    index = room_no - 1

    if rooms[index][2] == 0:
        print("Room not available.")

    else:

        rooms[index][2] = 0

        total_cost = rooms[index][1] * 3

        booked_count += 1
        revenue += total_cost

        print(
            f"Booking confirmed! {rooms[index][0]} room for 3 nights."
        )

        print(f"Total cost: {total_cost} yen")


print("\nTotal rooms booked :", booked_count)
print("Total revenue :", revenue, "yen")