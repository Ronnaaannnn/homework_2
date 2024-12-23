"""Take a student's marks as input. If the marks are more than 50, check if they are
greater than 90. If so, print "Excellent". If between 51 and 90, print "Good".
Otherwise, print "Fail"."""
marks=int(input("kati aayo tero "))
if marks > 90 :
    print ("excellent")
elif marks > 50 and marks < 90 :
    print ("good")
else :
    print ("fail")