import time
def main():

    dur = time.time()
    start = -300
    begin = ""
    print("Welcome to the bellwork timer.")
    print("You will have 5 minutes to complete the bellwork")
    print("Multiply your remaining seconds by 18.5 to get your score! (5k points max.)")
    begin = input("Press enter to start.")
    if begin == "":

        while start < 0:
            time.sleep(1)
            start += 1
            print(start)



if __name__ == "__main__":
    main()
