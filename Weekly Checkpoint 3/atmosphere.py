def main():

    layer = input("Descent atmosphere layer: ")
    if layer == "Troposphere":
        vt = 20
        at = 12000
        tr = 600
        print("Your altitude level will be between 0 and 12 km.")

    elif layer == "Stratosphere":
        vst = 75
        ast = 38000
        tstra = 506.7
        print("Your altitude level will be between 12 and 50 km")

    elif layer == "Mesosphere":
        vmes = 200
        ames = 35000
        tmes = 175
        print("Your altitude level will be between 50 and 85 km")

    elif layer == "Thermosphere":
        vthe = 500
        athe = 615000
        tthe = 230
        print("Your altitude level will be between 85 and 700 km")

    elif layer == "Exosphere":
        vex = 2000
        aexo = 1300000
        texo = 0
        print("Your altitude level will be between 700 and 2000 km")

    else:
        print("Type a valid input for the layer.")

    ea = float(input("Enter exact altitude (km): "))
    if ea <= 12:
        vt = 20
        ea = (ea / (vt / 1000))
        print(f"Total descent time: {vt}s")

    elif ea >= 13:
        vst = 75
        ea = (ea / (vst / 1000)) + 600
        print(f"Total descent time: {ea}s")

    elif ea >= 50:
        vmes = 200
        ea = (ea / (vmes / 1000)) + 506.5 + 600
        print(f"Total descent time: {ea}s")

    elif ea >= 85:
        vthe = 500
        ea = (ea / (vthe / 1000)) + 175 + 506.5 + 600
        print(f"Total descent time: {ea}s")

    elif ea >= 700:
        vex = 2000
        ea = (ea / (vex / 1000)) + 230 + 175 + 506.5 + 600
        print(f"Total descent time: {ea}s")

    else:
        print("Error, worng input.")

if __name__ == "__main__":
    main()
