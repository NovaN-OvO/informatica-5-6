def main():

    #Easy "If" level
    inte = int(input("Give me an integer number: "))
    if inte < 0:
        print(inte * (-1))
    else:
        print(inte)
    print()

    #Medium "If" level
    num1 = float(input("Give me a number: "))
    num2 = float(input("Give me another number: "))
    oper = input("What operation do you want to make ( +, -, *, / )? ")
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"
    if oper == add:
        print(num1 + num2)
    elif oper == sub:
        print(num1 - num2)
    elif oper == mul:
        print(num1 * num2)
    elif oper == div:
        print(num1 / num2)
    else:
        print()
        print("Invalid option you donut.")
    print()


if __name__ == "__main__":
    main()
