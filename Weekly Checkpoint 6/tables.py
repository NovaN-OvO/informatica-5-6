def main():
    while True:
        num = int(input("Enter a number (1-10): "))
        if num < 0:
            print("Type a number from 1 to 10.")
            continue
        if num <= 10:
            print(f"Here is {num} times table.")
            for i in range(10):
                print(f"{i+1} times {num} is {(i+1) * num}")
            des = input("Do you want to add another number ior exit? ").strip().lower()
            if des == "add":
                continue
            elif des == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        else:
            print("Type a number from 1 to 10.")
if __name__ == "__main__":
    main()
