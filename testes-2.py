def main():
    # In a range(x) you can use up to 3 values and they will work as:
    # range(10) 10 will be the numeber of values in a list
    # range(3, 10) 3 will work as a start, and 10 as an endpoint
    # range (1, 11, 2) start, end and the last number will be used as the increment. 1 > 3 > 5 > 7...11
    print("Times Table Quiz")
    i = True
    score = 0
    while i:
        try:
            max_value = int(input("Enter a times table that you would like to be tested on (1-10): "))
            if max_value >= 1 and max_value <= 10:
                max_test = int(input("Enter how many multiplications you want to be tested (1-10): "))
                if max_test >= 1 and max_test <= 10:
                    for x in range(1, max_test + 1):
                        try:
                            res_u = int(input(f"{x} times {max_value} is "))
                            if res_u == (x * max_value):
                                print("Correct.")
                                i = False
                                score += 1
                            else:
                                print("Incorrect.")

                        except ValueError:
                            print("You didn't enter a number.")
        except ValueError:
            print("You didn't enter a number.")
    print(f"Your score is {score}/{max_test}")
    print(f"({(score / max_test) * 100}%)")
if __name__ == "__main__":
    main()
