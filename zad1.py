cena = float(input("cena"))
sztuki = int(input("sztuki"))

wartosc = cena * sztuki

koszt_dostawy = 12

if wartosc > 100:
    koszt_dostawy = 0

lacznie=koszt_dostawy+wartosc

print(wartosc)
print(koszt_dostawy)
print(lacznie)
