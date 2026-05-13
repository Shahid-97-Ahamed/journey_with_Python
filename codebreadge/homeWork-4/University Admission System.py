# 23. University Admission System
gpa =float(input("Enter Your GPA: "))
ielts_score =float(input("Enter Your IELTS Score: "))
if gpa >= 3.5 and ielts_score >=6.5:
    print("Eligible for admission")
elif gpa < 3.5:
    print("GPA requirement not met")
else:
    print("IELTS requirement not met")