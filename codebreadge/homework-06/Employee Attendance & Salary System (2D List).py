employees = [
    ["aiko yamamoto", 28, 2000],
    ["kenji mori", 18, 1500],
    ["hana sato", 22, 1800],
    ["riku tanaka", 26, 2500]
]

print("=" * 50)
print("MONTHLY PAYROLL REPORT")
print("=" * 50)
print("Name | Days | Daily Wage | Salary | Status")
print("-" * 50)

index = 0
total_payroll = 0

while index < len(employees):

    name = employees[index][0]
    days_present = employees[index][1]
    daily_wage = employees[index][2]

    salary = days_present * daily_wage

    if days_present < 20:
        salary = salary * 0.90
        status = "Deducted"

    elif days_present >= 26:
        salary = salary * 1.05
        status = "Bonus"

    else:
        status = "Standard"

    total_payroll += salary

    print(
        name.title(), "|",
        days_present, "|",
        daily_wage, "|",
        int(salary), "|",
        status
    )

    index += 1

print("-" * 50)
print("Total Payroll:", int(total_payroll))