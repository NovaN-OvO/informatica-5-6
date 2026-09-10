from datetime import datetime
def main():
    day = datetime.now().weekday()
    days = ["Monday","Tuesday","Wednessday","Thursday","Friday","Saturday","Sunday"]
    #a valid list can be x = ["Hello", 2, 3.1415926535]
    print(day)
    print(days[day])
    if day < 4: #the day is a week day
        print("It's a weekday")
        remaining = 5 - day
        print(f"{remaining} days until the weekend.")
    elif day == 4:
        print("It's Friday")
        print("Just a day left until the weekend")
    else:
        print("It's the weekend!")
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    print("These are the summer months:")
    print(months[5])
    print(months[6])
    print(months[7])
    month = datetime.now().month
    print(f"It is {months[month-1]}")
if __name__ == "__main__":
    main()
