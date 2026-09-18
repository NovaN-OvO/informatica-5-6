def main():
    pyramid = int(input("Enter the height of the pyramid: "))
    asterisco = "*"
    espacio = " "
    for h in range(pyramid):
        print((espacio * (pyramid - (h+1))) + (asterisco * (h+1)) + (asterisco * (h+1)))
if __name__ == "__main__":
    main()
