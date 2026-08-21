def main():
    width = int(input("Enter the width of the rectangle: "))
    print("O" * width)
    print("O" * width)
    print("O" * width)
    print("O" * width)
    print("O" * width)

    # USE VARIABLES YOU DONUT!!!
    # p = (5 + width) * 2
    # a = 5 * width
    # d = ((5 ** 2) + (width ** 2 )) ** 0.5

    print(f"The perimeter of the are is equal to: ", (5 + width) * 2 )
    print(f"The area of the are is equal to: ", 5 * width )
    print(f"The diagonal of the area is equal to: ", ((5 ** 2) + (width ** 2 )) ** 0.5)
if __name__ == "__main__":
    main()
