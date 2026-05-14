# 28. AI Course Enrollment System
skill_level =input("Enter Your Skill Level(beginner / intermediate / advanced): ").lower()
age =int(input("Enter Your Age: "))
if skill_level == "beginner" and age >= 18:
    print("Enrollment Approved")
elif skill_level == "intermediate" and age >= 16:
    print("Enrollment Approved")
elif skill_level == "advanced" and age >= 14:
    print("Enrollment Approved")
elif skill_level in ["beginner", "intermediate", "advanced"]:
    print("Enrollment Denied")
else:
    print("Invalid Input")