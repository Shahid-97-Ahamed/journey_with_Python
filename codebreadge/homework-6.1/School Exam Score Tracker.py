# 1. School Exam Score Tracker

grades = ['Grade 10', 'Grade 11']
subjects = ['Math', 'Science', 'English']

scores = [
    [
        [72, 85, 61, 90],
        [55, 48, 79, 83],
        [88, 91, 74, 65]
    ],
    [
        [95, 88, 77, 69],
        [60, 72, 85, 91],
        [45, 78, 83, 90]
    ]
]

highest_score = 0
highest_grade = ""
highest_subject = ""
highest_student = 0

failing_students = 0

print("=" * 40)
print("EXAM SCORE REPORT")
print("=" * 40)

g = 0
while g < len(scores):

    print("\nGrade:", grades[g])

    s = 0
    while s < len(scores[g]):

        total = 0
        st = 0

        print(subjects[s], "| Scores:", end=" ")

        while st < len(scores[g][s]):

            score = scores[g][s][st]

            print(score, end=" ")

            total += score

            if score > highest_score:
                highest_score = score
                highest_grade = grades[g]
                highest_subject = subjects[s]
                highest_student = st + 1

            if score < 50:
                failing_students += 1

            st += 1

        average = round(total / len(scores[g][s]), 1)

        print("| Average:", average)

        s += 1

    g += 1

print("\nHighest score:", highest_score)
print(
    "Grade:", highest_grade,
    "| Subject:", highest_subject,
    "| Student", highest_student
)

print("Failing students (below 50):", failing_students)