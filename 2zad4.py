temperatury = []

for i in range(1,8):
    temp = temperatury.append(int(input(f"dzien {i}: ")))


sr = sum(temperatury)/len(temperatury)
print("srednia: ", sr)
print("max: ", max(temperatury))
print("min: ", min(temperatury))

powyzej_sredniej = []

for j in temperatury:
    if j > sr:
        powyzej_sredniej.append(j)

print("dni powyzej sredniej: ", powyzej_sredniej)