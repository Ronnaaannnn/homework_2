print("Welcome to the Wizarding World!")
choice = input("Do you want to study 'spells' or 'potions'? ").strip().lower()
if choice == "spells":
    sub_choice = input("Do you want to 'practice magic' or 'compete in duels'? ").strip().lower()
    if sub_choice == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif sub_choice == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice == "potions":
    sub_choice = input("Do you want to 'brew an elixir' or 'create poison'? ").strip().lower()
    if sub_choice == "brew an elixir":
        print("You healed a village. You Win!")
    elif sub_choice == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
