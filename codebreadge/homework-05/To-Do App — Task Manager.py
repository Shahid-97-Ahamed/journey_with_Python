# 7. To-Do App — Task Manager
# Initial task list
list_of_task = ['Buy groceries', 'Call doctor', 'Pay bills']

# # Insert urgent task at the top
list_of_task.insert(0,'Submit report') 
# print(list_of_task)

# Remove completed task
list_of_task.remove('Call doctor')

# reaminning task all uppercase
print(list_of_task[0].upper())
print(list_of_task[1].upper())
print(list_of_task[2].upper())

# day summary
status = "Busy day ahead!" if len(list_of_task) > 2 else "Light day!"
print(status)
