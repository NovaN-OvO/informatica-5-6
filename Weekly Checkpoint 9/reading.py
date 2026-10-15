def main():
    # Read a file
    with open("sample.txt") as file:# with is a keyword that falls into the for, while, if, words.
        content = file.read()
        print(content)

    # Turn file into a list
    with open("sample.txt") as hoco_week: # hoco_week is a variable
        hoco_list = hoco_week.read().splitlines() #turns a doc into a list. "splitlines()" converts the text into a list
        print(hoco_list)
    for day in range(len(hoco_list)):
        print(f"Day {day +1 }: {hoco_list[day]}")
if __name__ == "__main__":
    main()
