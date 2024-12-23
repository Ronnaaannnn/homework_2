"""Take a number as input. Check if it is divisible by 2. If yes, further check if it is
divisible by 5. Print appropriate messages for each condition."""
a=int(input("number van"))
if a % 2 == 0:
    if a % 5 == 0:
        print (a," div by two and 5")
    else:
         print (a," div by two and not 5")
else:
    print(a," div by none two or 5")
    
        
    