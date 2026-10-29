print("======moj budzet======")
print("1. dodaj przychod")
print("2. dodaj wydatek")
print("3. histrioa operacji")
print("4. stan konta")
print("5. podsumowanie finansowe")

print("0. zakoncz")

while True:
    opcja = int(input("wybierz opcje: "))

    if opcja == 1:
        print("przychod")

    elif opcja == 2:
        print("wydatek")

    elif opcja == 3:
        print("historia")

    elif opcja == 4:
        print("stan")

    elif opcja == 5:
        print("podsumowanie")

    elif opcja == 0:
        break