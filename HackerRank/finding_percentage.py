n = int(input())
students = {}

for _ in range(n):
    line = input().strip().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    students[name] = marks

query_name = input().strip()
average = sum(students[query_name]) / len(students[query_name])

print(f"{average:.2f}")