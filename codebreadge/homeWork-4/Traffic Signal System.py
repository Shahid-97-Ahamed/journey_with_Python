# 19. Traffic Signal System
signal_color =input("Enter Your Signal Color: ").lower()
if signal_color == "green":
    print("Go")
elif signal_color == "yellow":
    print("Slow Down")
elif signal_color == "red":
    print("Stop")
else:
    print("Invalid Signal")