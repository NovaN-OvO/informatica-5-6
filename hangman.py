import random
def main():
    start_game("100words.txt")
def start_game(file):
    with open(file) as words_file:
        words_list = words_file.read().splitlines()
        random_word = random.choice(words_list)
        print(random_word)
if __name__ == "__main__":
    main()
