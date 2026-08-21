def main():
    transistors = 17800000000
    years = int(input("How many years do you want to predict? "))
    current_year = 2026

    if (current_year + years) >= 2030:
        print("The law is not valid.")
    else:
        transistors *= (2 ** (years / 2))
        print("This is the transistor prediction in", years, "years: ", round(transistors))
        print(f"This is the transistor prediction in {years} years: {round(transistors)}") #Use this one better
if __name__ == "__main__":
    main()
