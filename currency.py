def main():

    colp = int(input("What do you have left in Colombian Pesos? "))
    sol = int(input("What do you have left in Peruvian Sol? "))
    reais = int(input("What do you have left in Brazilian Reais? "))

    cu = colp * 0.00032
    su = sol * 0.30
    ru = reais * 0.19
    tu = (cu + su + ru)
    round(tu, 2)
    print(f"USD: ", tu)

    cm = colp * 0.0054
    sm = sol * 5.07
    rm = reais * 3.28
    tm = cm + sm + rm
    round(tm, 2)
    print(f"MXN: ", tm)

if __name__ == "__main__":
    main()
