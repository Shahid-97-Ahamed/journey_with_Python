# 27. Smart Attendance System
attendance =float(input("Input Your Attendance: "))
assignment_submission_status=input("Are You Compleate Assignment(yes/no): ").lower()
if attendance >= 75 and assignment_submission_status == "yes":
    print("Eligible for final exam")
elif attendance < 75:
    print("Not eligible (low attendance)")
else:
    print("Not eligible (missing assignment)")