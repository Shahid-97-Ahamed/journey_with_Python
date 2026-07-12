n = int(input())
students = []
for _ in range(n):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

grades = sorted(set([student[1] for student in students]))
second_lowest = grades[1] 
result = [student[0] for student in students if student[1] == second_lowest]
for name in sorted(result):
    print(name)