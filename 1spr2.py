print("======kalkulator=========")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. dzielenie")
print("5. potegowanie")
print("6. srednia z liczb")
print("0. zakoncz")

while True:
    opcja = int(input("wybierz opcje: "))

    if 1<=opcja<=5:
        x = int(input("podaj 1 liczbe: "))
        y = int(input("podaj 2 liczbe: "))

        if opcja == 1:
            print(f"{x} + {y} = {x+y}")
        elif opcja == 2:
            print(f"{x} - {y} = {x-y}")
        elif opcja == 3:
            print(f"{x} * {y} = {x*y}")
        elif opcja == 4:

            if y == 0:
                print("nie dziel przez 0 holero")
            else:
                print(f"{x} / {y} = {x/y}")

        elif opcja == 5:
            print(f"{x} ** {y} = {x**y}")

    elif opcja == 6:
        z = int(input("ile liczb: "))

        liczby_sr = []

        for i in range(z):
            liczb = int(input(f"podaj {i+1} liczbe: "))
            liczby_sr.append(liczb)

        print(f"srednia z liczb {liczby_sr} = {sum(liczby_sr) / len(liczby_sr)}")
        
    elif opcja == 0:
        break
