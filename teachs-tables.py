def main():
    while True:
        nums = []
        for i in range(1,11):
            nums.append(str(i)) # "str" = string
        times_table = input("Enter a number 1-10: ").lower().strip()

        if times_table == "exit":
            break

        elif times_table in nums:
            print(f"Here is the {times_table} times table. ")

            for x in range(1,11): #the loop wont go further the highest number, but it will start with the first one.
                result = int(times_table) * x # x is the name of the variable inide our loop. which is [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
                # and you can use int() to create a string into an integer...
                print(f"{x} times {times_table} is {result}")

        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()

