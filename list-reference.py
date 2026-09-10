def main():
    numbers = [3, 5, 17, 4, 7, 6]
    result1 = max(numbers)
    result2 = min(numbers)
    result3 = sum(numbers)
    print("The max() function is a function that returns the largest item from an iterable or the largest of two or more arguments.")
    print(f"Example: In a list of [3, 5, 17, 4, 7, 6], the max() function will return: {result1}") #this will also wok if we put it like this: print(max(10, 20, 5, 8))
    print()
    print("The min() function is a function that returns the smallest item from an iterable or the smallest of two or more arguments.")
    print(f"Example: In the same list, the min() function will return {result2}")
    print()
    print("The sum() function is a function that add up all the values in a iterable")
    print(f"Example: In the same list, the min() function will return {result3}")
if __name__ == "__main__":
    main()
