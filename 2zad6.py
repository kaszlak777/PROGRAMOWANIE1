zadania = []

while True:
    print("1. dodaj zadanie")
    print("2. wyswietl zadania")
    print("3. usun zadanie")
    print("4. liczba zadan")
    print("0. zakoncz")
    
    opcja = int(input("wybierz opcje: "))
    
    if opcja == 1:
        zad = input("podaj zadanie: ")
        zadania.append(zad)

        
    elif opcja == 2:
        if not zadania:
            print("brak zadan")
        else:
            for i in range(len(zadania)):
                print(f"{i + 1}. {zadania[i]}")

                
    elif opcja == 3:
        if not zadania:
            print("brak zadan")
        else:
            numer = int(input("Podaj numer zadania: "))

            if 1 <= numer <= len(zadania):
                zadania.pop(numer - 1)
                print("usunieto")
            else:
                print("nie ma takiego")

                
    elif opcja == 4:
        print(f"liczba zadan: {len(zadania)}")

        
    elif opcja == 0:
        print("dowidzenia")
        break
        
    else:
        print("nie ma takiej opcji")