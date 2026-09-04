import random

def main():

    name = input("Hello! what is your name? ")
    number = ""
    att = 6
    print(f"Well, {name} , I want you to guess my number.")
    diff = input("Choose a difficulty. (Easy, Medium, Hard.): ").strip().title()
    guess = ""

    if diff == "Easy":

        print("Guess 1-10")
        guess = ""
        number = random.randint(1,10)

        while guess != number:
            att -= 1
            guess = int(input("Take a guess (1-10): "))

            if att == 0:
                print("Game over.")
                print(f"My number was {number}")
                break

            elif guess > number:
                print(f"Your guess is too high. (Attempts left: {att})")

            elif guess < number:
                print(f"Your guess is too low. (Attempts left: {att})")
            else:
                print("You guessed right!")
                break
    elif diff == "Medium":

        print("Guess 1-100")
        guess = ""
        number = random.randint(1,100)

        while guess != number:
            att -= 1
            guess = int(input("Take a guess (1-100): "))

            if att == 0:
                print("Game over.")
                print(f"My number was {number}")
                break

            elif guess > number:
                print(f"Your guess is too high. (Attempts left: {att})")

            elif guess < number:
                print(f"Your guess is too low. (Attempts left: {att})")
            else:
                print("You guessed right!")
                break
    if diff == "Hard":

        print("Guess 1-1000")
        guess = ""
        number = random.randint(1,1000)

        while guess != number:
            att -= 1
            guess = int(input("Take a guess (1-1000): "))

            if att == 0:
                print("Game over.")
                print(f"My number was {number}")
                break

            elif guess > number:
                print(f"Your guess is too high. (Attempts left: {att})")

            elif guess < number:
                print(f"Your guess is too low. (Attempts left: {att})")
            else:
                print("You guessed right!")
                break

    if diff == "Impossible":

        att = 100
        print("Guess 1-1000000")
        guess = ""
        number = random.randint(1,1000000)

        while guess != number:
            att -= 1
            guess = int(input("Take a guess (1-1000000): "))

            if att == 0:
                print("Game over.")
                print(f"My number was {number}")
                break

            elif guess > number:
                print(f"Your guess is too high. (Attempts left: {att})")

            elif guess < number:
                print(f"Your guess is too low. (Attempts left: {att})")
            else:
                print("You guessed right!")
                break

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
