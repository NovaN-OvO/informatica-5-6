def main():
    zodiac = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Sanke", "Horse", "Goat/Sheep", "Monkey", "Rooster/Chicken", "Dog", "Pig/Boar"]
    u_year = input("Enter your birth year: ")
    conv_year = int(u_year)
    for i in len(zodiac):
        to_year = conv_year + 12
        if conv_year < 2026:
            conv_year += 12
            print(conv_year)
        else:
            print("Today is your chinese zodiac year!")

if __name__ == "__main__":
    main()
