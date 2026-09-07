import time
def main():

    start = 300
    begin = ""
    stop = ""

    while start > 0:
        begin = input("Press enter to start.")


        if begin == "":
            print("The timer has begun.")
            time.sleep(1)
            start -= 1
            stop = input("Press enter to stop.")
            if stop == "":
                start *= 3.33
                print(f"Your score is {start}!")
                if start >= 240:
                    print("Perfect score!")
                elif start > 180:
                    print("Great score!")
                elif start > 120:
                    print("Good score!")
                elif start > 60:
                    print("Okay score.")
                else:
                    print("Keep working.")
                break



if __name__ == "__main__":
    main()
