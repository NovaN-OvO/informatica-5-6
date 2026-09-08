import time
def main():

    dur1 = time.time()
    begin = ""
    print("Welcome to the bellwork timer.")
    print("You will have 5 minutes to complete the bellwork")
    begin = input("Press enter to finish the timer. ")
    if begin == "":

        dur2 = time.time()
        ttime = dur2 - dur1
        ttime = round(ttime, 0)
        print(f"It took you {ttime}s to finish the bellwork.")

        if ttime <= 300:
            points = (300 - ttime) * 18.5
            points = round(points, 0)
            print(f"Your score is: {points}")
            if points >= 5000:
                print("Impossible... You're a robot!")
            elif points > 3000:
                print("Good job!")
            elif points > 1500:
                print("Keep going!")
            else:
                print("Keep working!")

        else:
            print("Time's up!")



if __name__ == "__main__":
    main()
