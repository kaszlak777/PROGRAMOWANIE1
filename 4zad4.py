warsztat_python = set()
warsztat_ai = set()

while True:

    print("1. zapisz na pyhton")
    print("2. zapisz na ai")
    print("3. wyswietl uczestnikow")
    print("4. uczestnicy obu warsztatow")
    print("5. wszyscy unikalni uczestnicy")
    print("0. zakoncz")

    opcja = int(input("wybierz opcje: "))

    if opcja == 1:
        imie = input("imię: ")
        nazwisko = input("nazwisko: ")
        ziomek = (imie, nazwisko)
        warsztat_python.add(ziomek)


    elif opcja == 2:
            imie = input("imię: ")
            nazwisko = input("nazwisko: ")
            ziomek = (imie, nazwisko)
            warsztat_ai.add(ziomek)

    elif opcja == 3:
        print("python: ", warsztat_python)
        print("ai: ", warsztat_ai)

    elif opcja == 4:
        wspulni = warsztat_python & warsztat_ai
        print("uczestnicy obu warsztatow: ", wspulni)

    elif opcja == 5:
        wszyscy = warsztat_python | warsztat_ai
        print("wszyscy unikalni uczestnicy: ", wszyscy)

    elif opcja == 0:
        break