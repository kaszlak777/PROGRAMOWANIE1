ile = int(input("ile pomiarow chcesz wprowadzic? "))

pomiary = []

for i in range(ile):
    pomiar = input(f"pomiar {i+1}: ")
    pomiary.append(pomiar)

print(f"pierwszy pomiar: {pomiary[0]}")
print(f"ostatni pomiar: {pomiary[-1]}")

print(f"pierwsze 3 pomiary: {pomiary[:3]}")
print(f"ostatnie 3 pomiary: {pomiary[-3:]}")
print(f"co drugi pomiar: {pomiary[::2]}")
print(f"odwrocone: {pomiary[::-1]}")
print(f"original: {pomiary}")

kopy = pomiary.copy()
kopy[0]=0
print(f"kopia po zmianie: {kopy}")