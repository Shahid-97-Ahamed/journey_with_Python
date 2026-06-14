temps = []
while True:
    val = input("Enter temperature in C (or 'stop'): ")
    if val == "stop":
        break
    temps.append(float(val))

highest = temps[0]
lowest = temps[0]
Warnings = 0
index = 0

while index < len(temps):
    if temps[index] > highest:
        highest =temps[index]
    if temps[index] < lowest:
        lowest =temps[index]
    if temps[index] > 35:
        Warnings =Warnings +1
    index += 1

print("Highets:",highest)
print("Lowest:",lowest)
print("Heat warning (>35c):",Warnings)