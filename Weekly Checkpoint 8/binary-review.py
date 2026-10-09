def main():
    print("Binary to Decimal Converter")
    valid_bits = ["0", "1"]
    while True:
        correct_chars = 0
        binary_num = input("Enter your binary number: ")
        for char in binary_num:
            if char in valid_bits: #If each character is in the valid_num list:}
                correct_chars += 1
        if correct_chars == len(binary_num):
            break
        else:
            print("Invalid Input.")


    binary_to_decimal(binary_num)

def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = (decimal * 2) + int(bit)
    print(decimal)

if __name__ == "__main__":
    main()

