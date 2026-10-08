godziny = int(input("podaj czas parkowania (h): "))

if godziny <= 0:
    print("nieprawidlowe dane.")
else:
    if godziny <= 1:
        oplata = 5
    elif godziny <= 3:
        oplata = 12
    elif godziny <= 6:
        oplata = 20
    else:
        oplata = 30

    print("czas postoju:", godziny, "godziny")
    print("oplata za parking:", oplata, "zl")