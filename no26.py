a = int(input("Enter your age: "))
b = input("Enter your gender (M/F): ").strip().upper()
c = input("Enter membership type ('Monthly' or 'Yearly'): ").strip().capitalize()

if 18 <= a < 30:
    if b == 'M':
        if c == 'Monthly':
            t = 50
        elif c == 'Yearly':
            t = 500
        else:
            print("Invalid membership type")
            exit()
    elif b == 'F':
        if c == 'Monthly':
            t = 45
        elif c == 'Yearly':
            t = 450
        else:
            print("Invalid membership type")
            exit()
    else:
        print("Invalid gender input")
        exit()
elif 30 <= a <= 50:
    if c == 'Monthly':
        t = 60
    elif c == 'Yearly':
        t = 600
    else:
        print("Invalid membership type")
        exit()
elif a > 50:
    if c == 'Monthly':
        t = 40
    elif c == 'Yearly':
        t = 400
    else:
        print("Invalid membership type")
        exit()
else:
    print("Invalid age input")
    exit()

print(f"Membership Fee: Rs{t}")
