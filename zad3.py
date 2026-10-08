cena = float(input("cena: "))
rabat = float(input("rabat (%): "))

rabat_pln = rabat/100*cena
cena_final = cena - rabat_pln

print("cena poczatkowa: ", cena)
print("kwota rabatu: ", rabat_pln)
print("cena po rabacie: ", cena_final)

if rabat>=20:
    print("duza promocja!")
else:
    print("standardowa promocja.")

