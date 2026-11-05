def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if b == 0:
        return "nie dziel przez 0 holero"
    else:
        return a / b
def potegowanie(a, b):
    return a ** b
def srednia_z_liczb(liczby):
    return sum(liczby) / len(liczby)



def wyswietl_menu():
    print("======kalkulator=========")
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. mnozenie")
    print("4. dzielenie")
    print("5. potegowanie")
    print("6. srednia z liczb")
    print("0. zakoncz")

def main():
    wyswietl_menu()

    while True:
        opcja = int(input("wybierz opcje: "))

        if 1 <= opcja <= 5:
            x = int(input("podaj 1 liczbe: "))
            y = int(input("podaj 2 liczbe: "))

            if opcja == 1:
                print(f"{x} + {y} = {dodawanie(x, y)}")
            elif opcja == 2:
                print(f"{x} - {y} = {odejmowanie(x, y)}")
            elif opcja == 3:
                print(f"{x} * {y} = {mnozenie(x, y)}")
            elif opcja == 4:
                print(f"{x} / {y} = {dzielenie(x, y)}")
            elif opcja == 5:
                print(f"{x} ** {y} = {potegowanie(x, y)}")

        elif opcja == 6:
            z = int(input("ile liczb: "))
            liczby_sr = []

            for i in range(z):
                liczb = int(input(f"podaj {i + 1} liczbe: "))
                liczby_sr.append(liczb)

            print(f"srednia z liczb {liczby_sr} = {srednia_z_liczb(liczby_sr)}")

        elif opcja == 0:
            break

        else:
            print("niepoprawna opcja")


if __name__ == "__main__":
    main()

