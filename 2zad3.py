napoje = ["Woda", "Sok", "Cola"]
ceny = [3, 5, 6]
koszty=0

while True:
    print("1. Woda - 3 zl")
    print("2. Sok - 5 zl")
    print("3. Cola - 6 zl")
    print("0. Zakoncz")

    opcja = int(input("wybierz opcje: "))

    if opcja == 0:
        break

    elif 1<= opcja <= 3:
        print(f"wybrano: {napoje[opcja-1]}, cena: {ceny[opcja-1]} zl")
        koszty += ceny[opcja-1]

    else:
        print("nie ma takiej opcji")

print(f"laczne koszty: {koszty} pln")
