

def main():
    planet =input("Planet: ")
    #Names of variables must be simple and use "_"

    # Separation
    print("Hello", planet)
    # The comma "," is equal to a space in the parenthesis

    #Ending
    print("Hello", end=" ")
    print(planet)

    #Concatenation
    print("Hello " + planet)

    # Formatted String
    print(f"Hello {planet}")
    #Ill be using this one!

if __name__ == "__main__":
    main()
