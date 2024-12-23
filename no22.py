age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").strip().upper()
income = float(input("Enter your income: "))

if age >= 18 and age < 60:
    if gender == 'M':
        if income > 1000000:
            tax = income * 0.25
            print(f"Tax = 25%: {tax}")
        elif 500000 <= income <= 1000000:
            tax = income * 0.15
            print(f"Tax = 15%: {tax}")
        else:
            tax = income * 0.05
            print(f"Tax = 5%: {tax}")
    elif gender == 'F':
        if income > 1000000:
            tax = income * 0.30
            print(f"Tax = 30%: {tax}")
        elif 500000 <= income <= 1000000:
            tax = income * 0.20
            print(f"Tax = 20%: {tax}")
        else:
            tax = income * 0.10
            print(f"Tax = 10%: {tax}")
    else:
        print("Invalid gender input")
elif age >= 60:
    if income > 1000000:
        tax = income * 0.20
        print(f"Tax = 20%: {tax}")
    else:
        tax = income * 0.10
        print(f"Tax = 10%: {tax}")
else:
    print("Invalid age input")
