import random

def main():
    guess = input("What face of the coin do you predict you will get: ").strip().lower()
    coin = random.randint(1,2)

    if coin == 1:
        coin = "heads"
    else coin == 2:
        coin = "tails"

    print(f"Coin: {coin}") #print("coin: ", coin)

    if guess == coin:
        print("You won!")
    elif guess != coin:
        print("You lost.")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
