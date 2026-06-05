# 5. University Course Registration System

departments = ['Engineering', 'Business', 'Arts']

courses = [
    [
        ["Algorithms", 3, 30, 28],
        ["Networks", 3, 25, 25],
        ["Databases", 2, 35, 10],
        ["AI Basics", 4, 20, 20]
    ],
    [
        ["Marketing", 3, 40, 38],
        ["Finance", 3, 30, 30],
        ["Management", 2, 35, 20],
        ["Economics", 4, 25, 25]
    ],
    [
        ["History", 3, 30, 15],
        ["Philosophy", 3, 20, 20],
        ["Literature", 2, 25, 10],
        ["Fine Arts", 4, 20, 18]
    ]
]

print("=" * 44)
print("UNIVERSITY COURSE CATALOG")
print("=" * 44)

d = 0
while d < len(courses):

    print("Department:", departments[d])

    c = 0
    while c < len(courses[d]):

        course_name = courses[d][c][0]
        credits = courses[d][c][1]
        max_seats = courses[d][c][2]
        enrolled = courses[d][c][3]

        if enrolled < max_seats:
            status = "Open"
        else:
            status = "Full"

        print(
            str(c) + ".",
            course_name,
            "| Credits:", credits,
            "| Seats:", max_seats,
            "| Enrolled:", enrolled,
            "|", status
        )

        c += 1

    d += 1


successful_registrations = 0

while True:

    dept_no = int(input("Enter department number (0-2, or -1 to exit): "))

    if dept_no == -1:
        break

    course_no = int(input("Enter course number (0-3): "))

    course_name = courses[dept_no][course_no][0]
    max_seats = courses[dept_no][course_no][2]
    enrolled = courses[dept_no][course_no][3]

    if enrolled >= max_seats:
        print("Registration failed: Course is full.")

    else:
        courses[dept_no][course_no][3] += 1
        successful_registrations += 1

        print(
            "Registered successfully for",
            course_name + "!",
            "(Enrolled:",
            str(courses[dept_no][course_no][3]) + "/" + str(max_seats) + ")"
        )

print("Total successful registrations this session:", successful_registrations)