def main():
    pyramid = int(input("Enter the height of the pyramid: "))
    asterisco = "*"
    for h in range(pyramid):
        print(asterisco * (h+1))
if __name__ == "__main__":
    main()
