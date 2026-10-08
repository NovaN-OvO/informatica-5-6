def main():
    # Make a list of the user's input
    # 13 = 1101
    #list = [binary]
    print("Binary to Decimal Converter")
    binary = input("Enter a binary number: ")
    binary_to_decimal(binary)

def binary_to_decimal(num):
    make = []
    digit = len(make)
    for i in range(len(num)):
        make.append(int(num[i]))
        digit = len(make)
        digit2 = digit * make[i]
        decimal = digit2 + (2 ** i)


    print(decimal)

        #(6 * x) + (5 + 0)

if __name__ == "__main__":
    main()
