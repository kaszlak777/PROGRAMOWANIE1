haslo = "Python123"
l=0

while l!=3:
    pruba = input("podaj haslo: ")

    if(pruba == haslo):
        print("udane logowanie!!!!!!!!!!!!!!")
        break
    else:
        l+=1

        if l == 3:
            print("konta zablokowane")
        else:
            print("niepoprawne haslo. pozostale proby: ", 3-l)
