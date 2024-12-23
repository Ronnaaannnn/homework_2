print("Welcome to the Cybersecurity Mission!")
choice = input("Do you want to 'trace the hacker' or 'secure the system'? ").strip().lower()

if choice == "trace the hacker":
    sub_choice = input("Do you want to 'track their IP' or 'decode their message'? ").strip().lower()
    if sub_choice == "track their IP":
        print("You caught the hacker. You Win!")
    elif sub_choice == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice == "secure the system":
    sub_choice = input("Do you want to 'shut down the server' or 'upgrade the firewall'? ").strip().lower()
    if sub_choice == "shut down the server":
        print("The attack was stopped. You Win!")
    elif sub_choice == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")