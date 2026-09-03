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
        number = random.randint(1,20)

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
    elif diff == "Medium":
        print("Guess 1-100")
                guess = ""
                number = random.randint(1,20)

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

    elif diff == "Hard":
        print("Guess 1-10")
                guess = ""
                number = random.randint(1,20)

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
    else:
        

if __name__ == "__main__":
    main()
