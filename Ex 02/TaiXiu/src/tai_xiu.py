import random


def tai_xiu_game():
    print("---------TÀI XỈU GAME!---------\n")

    #khoi tao tien va thong ke
    money = 100
    wins = 0
    losses = 0

    def current_money():
        print(f"You currently have ${money}\n")

    def get_user_bet():
        while True:
            bet = input("Place your bet amount (must be <= your current money): ")
            try:
                bet = int(bet)
                if 0 < bet <= money:
                    return bet
                else:
                    print(f"Invalid amount! You have ${money}.")
            except ValueError:
                print("Please enter a valid number.")

    def get_user_guess():
        while True:
            guess = input("Guess (Tài(T)/Xỉu(X) -> ").capitalize()
            if guess in {"T", "X"}:
                return guess
            else:
                print("Invalid input! Please enter 'T' or 'X'.")

    def roll_dice():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        result = "Tài" if total > 5 else "Xỉu"
        print(f"Dice rolled: {die1} + {die2} = {total} -> {result}")
        return result

    #vong lap choi
    run = True
    while run and money > 0:
        current_money()
        bet = get_user_bet()
        guess = get_user_guess()
        money -= bet  #tru tien cuoc

        result = roll_dice()
        if guess == result:
            print(f"Congratulations! You won ${bet}.")
            money += bet * 2  #thang an gap doi
            wins += 1
        else:
            print(f"Sorry! You lost ${bet}.")
            losses += 1

        print(f"Total wins: {wins}, Total losses: {losses}")
        if money <= 0:
            print("You ran out of money! Game over.")
            break

        choice = input("Do you want to play again? (Y/N) -> ").upper()
        if choice != "Y":
            run = False

    print(f"\nGame Over! You have ${money}. Wins: {wins}, Losses: {losses}")


#run game
tai_xiu_game()
