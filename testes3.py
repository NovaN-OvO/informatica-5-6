import random
def main():

    start_game("100words.txt")

def start_game(file):
    with open(file) as words_file:
        words_list = words_file.read().splitlines()
        random_word = random.choice(words_list)

    print("Welcome to the Hangman Game!")
    lifes = 6
    # While here. while lifes != 0:
    for letters in range(len(random_word)):
        dash = "_ " * letters

    print(dash)
    guess = input("Guess a letter: ")
    right = bool(guess in random_word)

    if right == True:
        print(right)
        for search in range(len(random_word)):
            if guess == random_word[search]:
                print(f"{guess} is in position {search}")
        das_let = []
        for change in range(len(random_word)):
            if guess == random_word[change]:
                das_let.append(guess)
            else:
                das_let.append("_ ")
        print(das_let)

    else:
        lifes -= 1
        print(f"Lifes remaining: {lifes}")

if __name__ == "__main__":
    main()
