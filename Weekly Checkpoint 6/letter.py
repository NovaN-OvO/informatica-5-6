def main():
    names = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]
    for receiver in names: #you can also use "for receiver in names" aparently
        if receiver != "Princess Peach":
            print(f"""
            +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                Dear {receiver},

                You are cordially invited to a ball at
                Peach's Castle this evening, 7:00 PM.

                Sincerely,
                {names[5]}
            +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+""")

if __name__ == "__main__":
    main()
