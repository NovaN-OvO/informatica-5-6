import random
def main():
    print("MATEMAKINA!")
    star = "⭐"
    streak = 0
    a = ""
    b = ""
    op = ""
    answer = ""

    while streak != 3:
        a = random.randint(10,99)
        b = random.randint(10,99)
        op = a + b

        print(f"What is {a} + {b}?")
        answer = int(input("Your answer: "))
        if answer != op:
            print("Incorrect.")
            print(f"The answer was {op}")
            if streak > 0:
                streak -= streak
        elif answer == op:
            print("Correct!")
            streak += 1
            if streak == 1:
                star == star
            elif streak == 2:
                star = "⭐⭐"
            else:
                star = "⭐⭐⭐"

            print(f"Streak: {star}")

        elif streak == 3:
            break
        else:
            print("Invalid option.")




if __name__ == "__main__":
    main()
