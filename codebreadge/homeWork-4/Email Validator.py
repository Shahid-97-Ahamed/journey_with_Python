# 10. Email Validator
users_email =input("Enter Your Email: ")
check_containt =("@" in users_email and 
                 users_email.endswith("com"))#Note:this (.endwith) means ".com" alwayes uses last
message = "Valid Email" if  check_containt else "Invalid Email"
print(message)