# 24. Bank Loan Eligibility System
salary =int(input("Enter Your Salary: "))
job_experince_years =int(input("Enter Your Job Experince Years: "))
if salary >= 300000 and job_experince_years >= 2:
    print("Loan Approved")
elif salary < 300000:
    print("Salary requirement not met")
else:
    print("Experience requirement not met")
