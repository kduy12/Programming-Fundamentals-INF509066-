import random


def game():
    print("---------GUESS THE NUMBER!---------\n")
    money = 100
    wins = 0
    losses = 0

    def current_money():
        print(f"You currently have ${money}\n")

    def choose_level():
        while True:
            level = input("Choose your level: (E)asy / (M)edium / (H)ard -> ").upper()
            if level in {"E", "M", "H"}:
                return level
            else:
                print("Invalid input! Please enter E, M, or H.")

    def main_game(level):
        nonlocal money, wins, losses
        max_attempts = {"E": 10, "M": 6, "H": 3}[level]
        number = random.randint(1, 100)
        money -= 5
        print(f"\nYou have {max_attempts} attempts to guess the number between 1 and 100.")

        for attempt in range(1, max_attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}: Your guess -> "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number} correctly.")
                wins += 1
                return

        print(f"Sorry! You did not guess the number. It was {number}.")
        losses += 1

    run = True
    while run and money >= 5:
        current_money()
        level = choose_level()
        main_game(level)
        print(f"Total wins: {wins}, Total losses: {losses}")
        if money < 5:
            print("You don't have enough money to continue playing.")
            break
        choice = input("Do you want to play again? (Y/N) -> ").upper()
        if choice != "Y":
            run = False

    print(f"\nGame Over! You have ${money}. Wins: {wins}, Losses: {losses}")


game()
