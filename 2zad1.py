zakupy = []
ile = int(input("ile prodktow chcesz dodac? "))

for i in range(ile):
    nowy = input(f"produkt {i + 1}: ")
    zakupy.append(nowy)

print("lista: ", zakupy)
print("liczba produktow: ", ile)

usun = input("do usuniecia: ")
if usun in zakupy:
    zakupy.remove(usun)
else:
    print("nie ma takiego")

print("nowa lista: ", zakupy)