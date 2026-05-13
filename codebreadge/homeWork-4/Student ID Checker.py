# 20. Student ID Checker
student_id =str(input("Enter Your Student ID: "))
id_checker =student_id.startswith("260")
message = "Valid Student" if id_checker  else "Invalid Student"
print(message)