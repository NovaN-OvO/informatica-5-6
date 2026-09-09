import random

def main():
    coin = ["heads", "tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choice(coin)
        # ".choice(x)" picks a single choice.
        guess = input("Heads or tails? ").strip().lower()
        
        print(f"The coin landed on {flip}")

        if guess == flip:
            print("You won!")
            break
        else:
            print("You lost.")
            attempts -= 1
            print(f"Attempts left: {attempts}.")
            print()
            if attempts == 0:
                print()
                print("Game over.")
                break




if __name__ == "__main__":
    main()
