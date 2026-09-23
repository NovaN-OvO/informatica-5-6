def main():
    num = 1
    while num > 0:
        num = input("Enter a number (1-10) or exit: ").strip().lower()
        if num <= 10:
            print(f"Here is {num} times table.")
            for i in range(10):
                print(f"{i+1} times {num} is {(i+1) * num}")
        elif num == "exit":
            print("Goodbye!")
            break

        else:
            print("Type a number from 1 to 10.")
if __name__ == "__main__":
    main()
