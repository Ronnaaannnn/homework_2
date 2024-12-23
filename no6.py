"""Write a program to input three numbers and find the largest among them using nested
if-else."""
a=int(input (" number van"))
b=int(input (" number van"))
c=int(input (" number van"))
if a > c :
    if a > b :
        print (a," is gteatest")
    else:
        print (b," is gteatest")
else :
    if c < b :
        print (b," is gteatest")
    else:
        print (c," is gteatest")
