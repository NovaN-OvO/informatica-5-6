import time
def main():

    dur1 = time.time()
    start = -300
    begin = ""
    print("Welcome to the bellwork timer.")
    print("You will have 5 minutes to complete the bellwork")
    begin = input("Press enter to finish the timer. ")
    if begin == "":
        dur2 = time.time()
        ttime = dur2 - dur1
        round(ttime, 2)
        print(ttime)
        if ttime <= 300:
            points = (300 - ttime) * 16.6
            round(points, 2)
            print(points)



if __name__ == "__main__":
    main()
