import random

user_wins = 0
computer_wins = 0
options = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:")
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock=0 paper=1 scissors=2
    computer_picks = options[random_number]
    print(f"Computer Picked:{computer_picks}.")

    if (user_input == "Rock" and computer_picks == "Scissors") or \
            (user_input == "Paper" and computer_picks == "Rock") or \
            (user_input == "Scissors" and computer_picks == "Paper"):
        print("You won!")
        user_wins += 1
    elif (user_input == "Scissors" and computer_picks == "Rock") or \
            (user_input == "Rock" and computer_picks == "Paper") or \
            (user_input == "Paper" and computer_picks == "Scissors"):
        print("Computer won!")
        computer_wins += 1
    else:
        print("It's a tie!")

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")

print("Goodbye")
