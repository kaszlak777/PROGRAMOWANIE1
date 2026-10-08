wiek = int(input("wiek: "))

dok = input("czy masz dokument?" )

if wiek >= 18 and dok == "tak":
    print("wypozyczenie mozliwe")
elif 13 <= wiek <= 17:
    opieka = input("czy masz zgode opiekuna? ")
    if opieka == "tak":
        print("wypozyczenie mozliwe")
    else:
        print("wypozyczenie niemozliwe")
else:
    print("wypozyczenie niemozliwe")