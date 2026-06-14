# marks = []


# while True:
#     users =input("Enter num: ").lower()
#     if users  == "stop":
#         break

#     marks.append(float(users))

# total = 0
# indx = 0
# while indx <len(marks):
#     total = total +marks[indx]
#     indx = indx +1

# if len(marks) > 0:
#     ave = total /len(marks)
#     print(f"class average: {ave}")
# else:
#     print("No marks were entered.")
    
# ---------------------------------5--------------------------------
# queue =[]

# while True:
#     users_name =input("Enter your name: ").lower()
#     if users_name == "start":
#         break
#     queue.append(users_name)

# while len(queue) > 0:
#     curr_per = queue[0]

#     queue.remove(curr_per)

#     print(f"Serving: {curr_per}. Remaining: {len(queue)}")


# ----------------------------6---------------------------------------------------

queue = []

while True:
    patient_add =input("")

    if patient_add == "quit":
        break
    elif patient_add == "next":
        patient =queue.pop(0)
        print(f"Calling: {patient}. Queue: {queue}")
    else:
        print("The queue is currently empty.")