def main():
    to_do = []
    start = input("Press enter to make your to-do list.")
    if start  == "":
        while to_do != 0:
            add_del = input("Do you want to add or complete an item to your list, or exit? ").strip().lower()
            if add_del == "add":
                to_do.insert(0, input("Add an item to your to-do list: ").strip().lower())
                print(to_do)
                print(f"You have {len(to_do)} taks left.")
            elif add_del == "complete":
                to_do.remove(input("Chose what item you want to complete: ").strip().lower())
                print(to_do)
                print(f"You have {len(to_do)} taks left.")
            elif add_del == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid option")

if __name__ == "__main__":
    main()
