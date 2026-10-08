def main():

    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)

def welcome():
    menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
    print("Welcome to In-and-Output!")
    print("Here's the menu:")
    for food in range(len(menu)):
        print(f"{food + 1}. {menu[food]}")

def get_item(order):
    if order == 1:
        print("🍔")
    elif order == 2:
        print("🍟")
    elif order == 3:
        print("🥤")
    elif order == 4:
        print("🍦")
    elif order == 5:
        print("🍪")
    else:
        print("Sorry, not in our menu.")
    # kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    #if 1 <= order <= 5:
        #print(kitchen[order - 1])
    #else:
        #print("Sorry, not in our menu.")

if __name__ == "__main__":
    main()
