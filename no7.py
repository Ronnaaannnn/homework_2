"""Write a program starting with "Welcome to the Jungle Survival Challenge".
 Ask the user to "search for food" or "build a shelter".
 If "search for food", ask to choose between "hunt" or "gather".
 If "hunt", print "You were attacked by a wild animal. Game Over."
 If "gather", print "You found enough food. You Win!"""


print("welcome to forest")
a=input("left or right :")
if a =="left":
    b=input(" explore or rest :")
    if b== "rest":
        print ("you died")
    elif b=="explore":
        print("you found treasure ")
    else :
        print("input valid")
else :
    print(" you die")
    
    