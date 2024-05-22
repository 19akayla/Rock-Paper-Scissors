import random
from colorama import Fore

Bank = 0
# Bank for the user

Bank_2 = 0
# Bank for the computer

rounds = 5  # Number of rounds

print("\tHello, this is the rock paper scissors game.")

for j in range(rounds):
#For loop for the rounds
    print()

    print("The rules of the game are that you type R, S, or P.")
    # Rules of the game
    print()
    rules = print(Fore.BLACK + "R beats P, P beats S, S beats R." + Fore.RESET)
    print()

    print(f"You have entered round {j + 1}")
    print()
    computer = random.choice(["r", "p", "s"])
    print("Enter r for rock, s for scissors, and p for paper")
    answer = input().lower()
    if answer == computer:
        print("It's a tie")
        print("You can now play heads or tails")
        HT = random.choice(["H", "T"])
        # Compare user input to computer random choice
        choice = input("Enter H for heads and T for tails: ").lower()
        if choice == "h" and HT == "h" or choice == "t" and HT == "t":
            print()
            print(Fore.GREEN + "You WON" + Fore.RESET)
            Bank += 1
            print("Your points are now", Bank)
        elif choice == "h" and HT == "t" or choice == "t" and HT == "h":
            print()
            print(Fore.RED + "You lost, the computer won" + Fore.RESET)
            Bank_2 += 1
            print(Fore.GREEN, "The computer's points are now", Bank_2, Fore.RESET)
    elif answer == "r" and computer == "p" or answer == "p" and computer == "s":
        print()
        print(Fore.RED + "You lost, the computer won" + Fore.RESET)
        Bank_2 += 1
        print(Fore.GREEN, "The computer's points are now", Bank_2, Fore.RESET)
    elif answer == "r" and computer == "s" or answer == "s" and computer == "p":
        print()
        print(Fore.GREEN + "You WON" + Fore.RESET)
        exit()
    else:
        exit()
    print()
