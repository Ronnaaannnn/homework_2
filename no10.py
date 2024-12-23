"""10. Start with "Welcome to the Haunted Castle".
 Ask the user to choose "enter the castle" or "run away".
 If "enter the castle", ask them to choose a door: "red", "green", or "black".
o If "red", print "You entered a room full of flames. Game Over."
o If "green", print "You found the treasure. You Win!"
o If "black", print "You were captured by ghosts. Game Over."
 If "run away", print "You escaped safely."""

print("Welcome to the Haunted Castle")
choice1 = input("Do you want to 'enter the castle' or 'run away'? ").lower()
if choice1 == "enter the castle":
  print("You approach the castle. There are three doors: red, green, and black.")
  choice2 = input("Which door do you choose? (red, green, or black) ").lower()
  if choice2 == "red":
    print("You entered a room full of flames. Game Over.")
  elif choice2 == "green":
    print("You found the treasure! You Win!")
  elif choice2 == "black":
    print("You were captured by ghosts. Game Over.")
  else:
    print("Invalid door choice. Game Over.")
elif choice1 == "run away":
  print("You escaped safely.")
else:
  print("Invalid choice. Game Over.")