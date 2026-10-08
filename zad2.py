pkt = int(input("pkt: "))
if 0<=pkt<=49:
    print("ocena: 2.0")
elif 50<=pkt<=59:
    print("ocena: 3.0")
elif 60<=pkt<=69:
    print("ocena: 3.5")
elif 70<=pkt<=79:
    print("ocena: 4.0")
elif 80<=pkt<=89:
    print("ocena: 4.5")
elif 90<=pkt<=100:
    print("ocena: 5.0")
elif pkt>100:
    print("bledne dane")