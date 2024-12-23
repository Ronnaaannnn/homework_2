age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").strip().upper()
score = float(input("Enter your academic score (out of 100): "))

if 18 <= age <= 25:
    if gender == 'M':
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == 'F':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    else:
        print("Invalid gender input")
else:
    print("Not eligible for scholarship based on age.")
