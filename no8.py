"""Write a program starting with "Welcome to the Jungle Survival Challenge".
 Ask the user to "search for food" or "build a shelter".
 If "search for food", ask to choose between "hunt" or "gather".
 If "hunt", print "You were attacked by a wild animal. Game Over."
 If "gather", print "You found enough food. You Win!"""
print("Welcome to the Jungle Survival Challenge")
choice1 = input("Do you want to 'search for food' or 'build a shelter'? ").strip().lower()
if choice1 == "search for food":
    choice2 = input("Do you want to 'hunt' or 'gather'? ").lower()
    if choice2 == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice2 == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice.  'hunt' or 'gather'.")

elif choice1 == "build a shelter":
    print("You built Try again tomorrow!")
else:
    print("Invalid choice.")
