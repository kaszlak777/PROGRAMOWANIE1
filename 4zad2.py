ile = int(input("podaj liczbe produktow: "))

produkty = []
ceny = []

for i in range(ile):
    produkt = input(f"produkt {i+1}: ")
    cena = float(input(f"cena {i+1}: "))
    produkty.append(produkt)
    ceny.append(cena)

for numer, produkt in enumerate(produkty, start=1):
    print(numer, produkt)

for produkt, cena in zip(produkty, ceny):
    print(produkt, cena)

sumaaaa = sum(ceny)
print(f"suma cen: {sumaaaa}")
print(f"najdrozzy produkt: {max(ceny)}")