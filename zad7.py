kwota = float(input("ile odkladasz tygodniowo? "))

tyg = int(input("przez ile tygodni? "))

oszczednosci = 0


for tydzien in range(1, tyg + 1):
    oszczednosci = oszczednosci + kwota
    
    print("tydzien", tydzien, ": ", oszczednosci, "zl")


print("laczne oszczednosci:", oszczednosci, "zl")
