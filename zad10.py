studenci = int(input("ile masz studentow? "))

zaliczone = 0

for s in range(studenci):

    nazwisko = input("nazwisko: ")
    pkt = int(input("pkt: "))

    if 0<=pkt<=49:
        print(nazwisko, " - ", pkt, " pkt - ocena 2.0")
    elif 50<=pkt<=59:
        print(nazwisko, " - ", pkt, " pkt - ocena 3.0")
        zaliczone+=1
    elif 60<=pkt<=69:
        print(nazwisko, " - ", pkt, " pkt - ocena 3.5")
        zaliczone+=1
    elif 70<=pkt<=79:
        print(nazwisko, " - ", pkt, " pkt - ocena 4.0")
        zaliczone+=1
    elif 80<=pkt<=89:
        print(nazwisko, " - ", pkt, " pkt - ocena 4.5")
        zaliczone+=1
    elif 90<=pkt<=100:
        print(nazwisko, " - ", pkt, " pkt - ocena 5.0")
        zaliczone+=1
    elif pkt>100:
        print("bledne dane")

print("zaliczylo: ", zaliczone, " studentow")





