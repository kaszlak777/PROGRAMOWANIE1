p = int(input("poczatek: "))
k = int(input("koniec: "))

x=0

for i in range(p, k+1):

    if i%2==0:
        print(i, " - parzysta")
        x+=1
    else:
        print(i, " - nieparzysta")

print("liczba liczb parzystych: ", x)