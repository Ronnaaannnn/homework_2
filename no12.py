print("Welcome to the Pirate Ship Adventure!")
choice = input("Do you want to 'search for treasure' or 'battle enemy ships'? ").strip().lower()

if choice == "search for treasure":
    sub_choice = input("Do you want to 'dig on the island' or 'explore the cave'? ").strip().lower()
    if sub_choice == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif sub_choice == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice == "battle enemy ships":
    sub_choice = input("Do you want to 'attack' or 'defend'? ").strip().lower()
    if sub_choice == "attack":
        print("You won the battle. You Win!")
    elif sub_choice == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")