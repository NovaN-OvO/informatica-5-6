def main():
    spn = int(input("Spain goals: ")) #
    arg = int(input("Argentina goals: "))

    if spn > arg:
        print("Spain is the winner!")
    elif arg > spn:
        print("Argentna is the winner!")
    else:
        print("It's a tie")

    print("GG.")

if __name__ == "__main__":
    main()
