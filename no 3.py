"""Take an employee's monthly salary as input. If it's more than 50,000, classify as
"High Earner". If less than or equal to 50,000, check if it's more than 20,000 to
classify as "Mid Earner", else classify as "Low Earner"""
salary=int(input("enter your salary "))
if salary >= 50000:
    print(" high earner ho yo with ",salary," ko kamai ")
elif salary >= 20000 and salary <= 50000:
    print("middle class eraner with ",salary, " ko paisa")
else:
    print (f"the manchey is low earner with {salary} ko paisa")
    