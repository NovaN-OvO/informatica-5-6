def main():
    # Select your lines, ctrl + k + c to make them a comment, ctrl + k + u to undo the comments.
    print("Your must enter a NUMBER. ")
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1-10: "))
            if number >= 1 and number <= 10:
                print("Number stored successfully")
                not_validated = False
            else:
                print("That number is not between 1-10. Try again.")
        except ValueError:
            print("You didn't entered a number.")
            not_validated = True
    while True:
        try:
            name = input("Enter your name: ") # Strings are lists too.
            f_letter = name[0]
            print("Name stored successfully.")
            break
        except IndexError:
            print("A name is required.")
    # name = 0
    # while name != "":
    #     name input("Enter your namee: ")
    #     if name == "":
    #         print("A name is required.")
    #         name = 0
    #     else:
    #         print("Name stored successfully.")
    #         break
    # sometimes try and execpt are not necesary but it does has its functions and utilities.
if __name__ == "__main__":
    main()
