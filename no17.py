color = input("Enter a color: ").strip().lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow Down")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")
