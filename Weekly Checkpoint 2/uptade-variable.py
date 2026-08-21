def main():

    # Agumented Assignment Operator
    # It combines a mathematical value with variables
    money = 5
    money += 10
    # "+=" adds value to the variavle
    print(money) #This will print 15

    #Substraction Assignment Operator
    minutes = 60
    minutes -= 25
    print(minutes) #This will print 35

    #Multiply Assignment Operator
    skill = 10
    skill *= 4
    text = "Im Lauro "
    text *= 7
    print(skill)
    print(text)

    #Division Asisgnmment Operator
    pizza = 8
    people = int(input("People at the pizza party: "))
    pizza /= people
    print(pizza)


    #Modulus Assignment Operator
    num1 = 10 
    num2 = 5
    num1 %= num2
    print(num1)

if __name__ == "__main__":
    main()
