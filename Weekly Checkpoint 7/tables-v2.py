def main():
    # In a range(x) you can use up to 3 values and they will work as:
    # range(10) 10 will be the numeber of values in a list
    # range(3, 10) 3 will work as a start, and 10 as an endpoint
    # range (1, 11, 2) start, end and the last number will be used as the increment. 1 > 3 > 5 > 7...11
    print("Times Table Quiz")
    i = True
    while i:
        try:
            max_value = int(input(f"Enter a times table that you would like to be tested on (1-10): "))
            for x in range(1, max_value + 1):
                try:
                    res_u = int(input(f"{x} times {max_value} is "))
                    if res_u == (x * max_value):
                        print("Correct.")
                        i = False
                    else:
                        print("Incorrect.")
                except ValueError:
                    print("You didn't enter a number.")
        except ValueError:
            print("You didn't enter a number.")

if __name__ == "__main__":
    main()
