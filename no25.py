a = int(input("Enter your age: "))
b = input("Enter your gender (M/F): ").strip().upper()
c = input("Enter show type ('Matinee' or 'Evening'): ").strip().capitalize()

if a < 12:
    if c == 'Matinee':
        t = 500
    elif c == 'Evening':
        t = 700
    else:
        print("Invalid show type")
        t = None
elif 12 <= a < 60:
    if b == 'M':
        if c == 'Matinee':
            t = 800
        elif c == 'Evening':
            t = 1000
        else:
            print("Invalid show type")
            t = None
    elif b == 'F':
        if c == 'Matinee':
            t = 700
        elif c == 'Evening':
            t = 900
        else:
            print("Invalid show type")
            t = None
    else:
        print("Invalid gender input")
        t = None
else:
    t = 600

if t is not None:
    print(f"Ticket Price: Rs{t}")
