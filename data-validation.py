def main():
    print("Your must enter a NUMBER. ")
    not_validated = True
    while not_validated:

        try:
            number = int(input("Enter a number between 1-10: "))

            if 1 <= number <= 10:
                print("Number stored successfully")

            else:
                print("Enter a number BETWEEN 1-10: ")
                continue

            not_validated = False

        except ValueError:
            print("You didn't entered a number.")
            not_validated = True

if __name__ == "__main__":
    main()
