iles = int(input("ile masz studentow? "))
punkty = []
zal=0

for i in range(iles):
    pkts = int(input(f"punkty studenta {i+1}: "))
    punkty.append(pkts)

print("srednia: ", sum(punkty)/len(punkty))
print("najwyzszy wynik: ", max(punkty))
print("najnizszy wynik: ", min(punkty))
print("wyniki rosnaco: ", sorted(punkty))

for i in punkty:
    if i>=50:
        zal+=1

print("zaliczylo: ", zal)
