print("======bibloteka=======")
print("1. dodaj ksionke")
print("2. wyswietl wszystkie ksiaszki")
print("3. wypozyc")
print("4. zwroc")
print("5. usun ksiaszke")
print("0. zakoncz")

ksiazki = []

while True:
    opcja = int(input("wybierz opcje: "))

    if opcja == 1:
        tytul = input("tytul: ")
        autor = input("autor: ")

        ksionsz = {
            "tytul": tytul,
            "autor": autor,
            "dostepna": True
        }

        ksiazki.append(ksionsz)

    elif opcja == 2:
        if not ksiazki:
            print("brak ksionzek")

        else:
            for i, k in enumerate(ksiazki):
                print(f"{i + 1}. tytul: {k['tytul']}, autor: {k['autor']}, dostepna: {k['dostepna']}")

    elif opcja == 3:
        if not ksiazki:
            print("brak ksionzek")

        else:
            nr = int(input("numer ksionzki: "))

            if 1 <= nr <= len(ksiazki):

                if ksiazki[nr - 1]["dostepna"]:

                    ksiazki[nr - 1]["dostepna"] = False
                    print("wypozyczono")
                else:
                    print("niedostepna aktualnie bo ktos wypozyzyl")

            else:
                print("nie ma takiej ksionzki")

    elif opcja == 4:
        if not ksiazki:
            print("brak ksionzek")

        else:
            nr = int(input("numer ksionzki: "))

            if 1<= nr <= len(ksiazki):

                if ksiazki[nr - 1]["dostepna"] == False:

                    ksiazki[nr - 1]["dostepna"] = True
                    print("zwrociles")

    elif opcja == 5:
        if not ksiazki:
            print("brak ksionzek")

        else:
            nr = int(input("numer ksionzki: "))

            if 1 <= nr <= len(ksiazki):

                ksiazki.pop(nr - 1)
                print("usunieto ksionszk")

            else:
                print("nie ma takiej ksionzki")

    elif opcja == 0:
        break