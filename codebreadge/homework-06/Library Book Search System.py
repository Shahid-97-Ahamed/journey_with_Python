books = [
    "Python Crash Course",
    "Clean Code",
    "Atomic Habits",
    "The Pragmatic Programmer",
    "Deep Work"
]

search_count = 0

while True:

    search_book = input("Enter book title (or 'exit' to quit): ")

    if search_book.lower() == "exit":
        break

    search_count += 1

    found = False

    index = 0

    while index < len(books):

        if search_book.lower() == books[index].lower():
            found = True
            break

        index += 1

    if found:
        print("Book found!")

    else:
        print("Book not available.")

print("\nTotal searches made:", search_count)