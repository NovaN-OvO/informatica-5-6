def main():
    largest("numbers.txt")
def largest(file):
    with open(file) as num_file:
        num_list = num_file.read().splitlines()

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i]) #replacing the string with an integer

    print(max(num_list))
    print(min(num_list))
if __name__ == "__main__":
    main()
