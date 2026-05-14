# 29. Smart Parking System
vehicle_name =input("Enter Your Vihicle Name: ").lower()
parking_hours =int(input("Enter Your Parking Hours: "))
if vehicle_name == "bike":
    print("Total Fee: ",100 * parking_hours, "yen")
elif vehicle_name == "car":
    print("Total Fee: ",300 * parking_hours, "yen")
elif vehicle_name == "truck":
    print("Total Fee: ",500 * parking_hours, "yen")
else:
    print("Invalid vehicle type")
