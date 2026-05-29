train_names = ["Nozomi", "Hikari", "Kodama", "Sakura"]

seat_classes = [
    "Green",
    "Reserved",
    "Unreserved",
    "Standing",
    "Disabled"
]

seats = [
    [12, 45, 0, 0, 3],     # Nozomi
    [0, 10, 22, 15, 2],    # Hikari
    [5, 0, 30, 40, 0],     # Kodama
    [8, 20, 18, 0, 5]      # Sakura
]

print("=" * 40)
print("TRAIN SEAT AVAILABILITY")
print("=" * 40)

print(
    "Train | Green | Reserved | Unreserved | Standing | Disabled"
)

print("-" * 68)

index = 0

while index < len(train_names):

    print(
        train_names[index], "|",
        seats[index][0], "|",
        seats[index][1], "|",
        seats[index][2], "|",
        seats[index][3], "|",
        seats[index][4]
    )

    index += 1

while True:

    train_index = int(
        input(
            "\nEnter train number to check (0-3, or -1 to exit): "
        )
    )

    if train_index == -1:
        break

    print(f"\n--- {train_names[train_index]} Seat Status ---")

    class_index = 0

    while class_index < len(seat_classes):

        available_seats = seats[train_index][class_index]

        if available_seats > 0:
            print(
                seat_classes[class_index],
                ": Available",
                f"({available_seats} seats)"
            )

        else:
            print(
                seat_classes[class_index],
                ": Full"
            )

        class_index += 1

print("\nGoodbye!")