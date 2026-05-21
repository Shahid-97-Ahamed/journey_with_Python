# 3. Cinema Seat Booking
seats = [10,11,12,13,14,15,16]
# print first and last seates
print("First seats:",seats[0]," | last seats:",seats[-1])

# Slice 3 seats starting from index 2
booked_seat = seats[2:5]

# print booked seats
print("Booked seats:",booked_seat)

# Booking status 
message = "Booking confirmed for 3 seats!" if len(booked_seat) == 3 else "'Booking failed'."
print(message)