# 2. Hospital Waiting Queue

pre_defined_patient = ['Rin', 'Sam', 'Yuki']
# add new patient
pre_defined_patient.append("Leo")
#call and remove first paitent  
store_remove_name =pre_defined_patient.pop(0)
# print result
print("Now calling: ",store_remove_name)
print("Remaining queue: ",pre_defined_patient)
print("Patients waiting: ",len(pre_defined_patient))
