def main():

    layer = input("Descent atmosphere layer: ")
    if layer == "Troposphere":
        tro = 12000
        print("Your altitude level will be between 0 and 12 km.")
    elif layer == "Stratosphere":
        print("Your altitude level will be between 12 and 50 km")
    elif layer == "Mesosphere":
        print("Your altitude level will be between 50 and 85 km")
    elif layer == "Thermosphere":
        print("Your altitude level will be between 85 and 700 km")
    elif layer == "Exosphere":
        print("Your altitude level will be between 700 and 2000 km")
    else:
        print("Type a valid input for the layer.")

    ea = int(input("Enter exact altitude (km): "))
    




if __name__ == "__main__":
    main()
