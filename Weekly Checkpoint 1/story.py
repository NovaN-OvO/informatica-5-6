

def main():
    # planet =input("Planet: ")
    # #Names of variables must be simple and use "_"

    # # Separation
    # print("Hello", planet)
    # # The comma "," is equal to a space in the parenthesis

    # #Ending
    # print("Hello", end=" ")
    # print(planet)

    # #Concatenation
    # print("Hello " + planet)

    # # Formatted String
    # print(f"Hello {planet}")
    # Ctrl+K+C to make all selected to a comment

    name = input("What is your name? ").title().strip()
    color = input("Tell me a color: ").lower().strip()
    adj = input("Tell me an adjetive: ").lower().strip()
    goal = input("A goal you would like to achieve: ").lower().strip()
    print(f"Hello, {name}!")
    print()
    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.")
    print()
    print("This is your story:".upper())
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.".upper())
    #From ^........................................to.............................................................^ here
    # The stirng is the thing in the "print" function!


if __name__ == "__main__":
    main()
