import random

def main():

    name = input("Hello! what is your name? ")
    number = random.randint(1,100)
    att = 6
    print(f"Well, {name} , I am thinking of a number between 1 and 100.")
    guess = ""

    while guess != number:
        att -= 1
        guess = int(input("Take a guess: "))

        if att == 0:
            print("Game over.")
            break

        elif guess > number:
            print(f"Your guess is too high. (Attempts left: {att})")

        elif guess < number:
            print(f"Your guess is too low. (Attempts left: {att})")
        else:
            print("You guessed right!")
            break

if __name__ == "__main__":
    main()
