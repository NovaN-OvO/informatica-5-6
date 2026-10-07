def main():
    def highest(a, b):
        if a > b:
            highest_num = a
            print(f"The highest number entered is {highest_num}")
        else:
            highest_num = b
            print(f"The highest number entered is {highest_num}")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    highest(num1, num2)

    def lowest(a, b, c):
        if a < b and a < c:
            lowest_num = a
            print(f"The lowest number entered is {lowest_num}")
        elif b < a and b < c:
            highest_num = b
            print(f"The lowest number entered is {lowest_num}")
        elif c < a and c < b:
            highest_num = c
            print(f"The lowest number entered is {lowest_num}")
        else:
            print("You entred the same lowest number twice.")

    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))
    num5 = float(input("Enter the fifth number: "))

    lowest(num3, num4, num5)

if __name__ == "__main__":
    main()
