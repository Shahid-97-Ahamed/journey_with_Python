patients = []

while True:
    name = input("Enter patient name (or 'done'): ")

    if name.lower() == "done":
        break

    age = int(input("Enter age: "))
    severity = int(input("Enter severity (1-10): "))

    patients.append([name.title(), age, severity])

print("\n--- Patient Report ---")

priority_count = 0
normal_count = 0
standard_count = 0

index = 0

while index < len(patients):

    name = patients[index][0]
    age = patients[index][1]
    severity = patients[index][2]

    if age >= 60 or severity >= 7:
        status = "Priority Treatment"
        priority_count += 1

    elif age >= 18 and severity >= 4:
        status = "Normal Treatment"
        normal_count += 1

    else:
        status = "Standard Queue"
        standard_count += 1

    print(
        f"{name} | Age: {age} | Severity: {severity} -> {status}"
    )

    index += 1

print("Priority Treatment :", priority_count)
print("Normal Treatment :", normal_count)
print("Standard Queue :", standard_count)