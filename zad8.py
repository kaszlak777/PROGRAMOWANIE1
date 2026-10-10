height = int(input("wysokosc podaj: "))

spacje = height - 1

for x in range(height):
    print(" "*(spacje - x) + "*"*(2 * x +1))