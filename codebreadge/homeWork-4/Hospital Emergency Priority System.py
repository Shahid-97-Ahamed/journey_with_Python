# 25. Hospital Emergency Priority System
patient_age =int(input("Enter Patient Age: "))
emergency_level =int(input("Emergency Level: "))
if patient_age >= 60 or emergency_level >= 7:
    print("Priority Treatment")
elif patient_age >= 18 and emergency_level >= 4:
    print("Normal Treatment")
else:
    print("Standard Queue")