def main():

    answer = "" # < This is called "initialize"
    followup = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").strip().title() #This is the update,
        # Title converts every first letter to capital

        if answer == "Yes":
            followup = input("Really? ").strip().title()
        if followup == "Yes!":
            break


    print("We just arrived.")

if __name__ == "__main__":
    main()
