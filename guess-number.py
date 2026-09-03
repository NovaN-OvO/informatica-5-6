import random

def main():

    name = input("Hello! what is your name? ")
    number = random.randint(1,100)
    print(f"Well, {name} , I am thinking of a number between 1 and 100.")
    guess = ""

    while guess != number:
        guess = int(input("Take a guess: "))

        if guess > number:
            print(f"Your guess is too high.")

        elif guess < number:
            print(f"Your guess is too low.")
        else:
            print("You guessed right!")
            break

if __name__ == "__main__":
    main()
