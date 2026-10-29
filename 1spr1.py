print("========Ksiazak kontaktow========")
print("1. dodaj kontakt")
print("2. wyswietl kontakty")
print("3. wyszukaj kontakt")
print("4. edytuj kontakt")
print("5. usun kontakt")
print("0. zakoncz")
print("=================================")

kontakty = []

while True:

    opcja = int(input("wybierz opcje: "))

    if opcja == 1:
        imie = input("imie: ")
        nazwisko = input("nazwisko: ")
        telefon = input("nr telefonu: ")

        print("kontakt dodany")

        kontakt = {
            "imie": imie,
            "nazwisko": nazwisko,
            "telefon": telefon }

        kontakty.append(kontakt)

    elif opcja == 2:
        if not kontakty:
            print("brak kontaktow")
        else:
            for i, kontakt in enumerate(kontakty):
                print(f"{i + 1}. {kontakt['imie']} {kontakt['nazwisko']} - {kontakt['telefon']} ")

    elif opcja == 3:
        if not kontakty:
            print("brak kontaktow")
        else:
            szukaj_tel = input("podaj nr telefonu do wyszuania: ")
            znal_kontakt = [k for k in kontakty if k["telefon"] == szukaj_tel]

            if znal_kontakt:
                for k in znal_kontakt:
                    print(f"{k['imie']} {k['nazwisko']} - {k['telefon']}")
            else:
                print("nie znaleziono kontaktu")

    elif opcja == 4:
        if not kontakty:
            print("brak kontaktow")

        else:
            nr = int(input("nr kontaktu do edytowania: "))

            if 1 <= nr <= len(kontakty):
                kontakt = kontakty[nr - 1]

                print(f"edycja kontaktu: {kontakt['imie']} {kontakt['nazwisko']} - {kontakt['telefon']}")

                imie = input("nowe imie: ")
                nazwisko = input("nowe nazwisko: ")

                
                kontakt["imie"] = imie
                
                kontakt["nazwisko"] = nazwisko


                print("kontakt zaaktualizowany")
            else:
                print("nie ma takiego")

    elif opcja == 5:
        if not kontakty:
            print("brak kontaktow")

        else:
            nr = int(input("nr do usuniecia: "))

            if 1 <= nr <= len(kontakty):

                kontakty.pop(nr - 1)
                print("usunieto")

            else:
                print("nie ma takiego")

    elif opcja == 0:
        break