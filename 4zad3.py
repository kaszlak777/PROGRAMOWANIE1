ile = int(input("ile pomiarow? "))

pomiary = []

for i in range(ile):
    pomiar = int(input(f"pomiar {i+1}: "))
    pomiary.append(pomiar)


alarmsy = [x for x in pomiary if x > 50]
print(f"alarmowe: {alarmsy}")

drugalista = [x * 2 for x in pomiary]
print(f"podwojone: {drugalista}")

alarmsss = any(x > 50 for x in pomiary)
print(f"czy wystopil alarm? {'tak' if alarmsss else 'nie'}")

alarmyyyys = all(x <= 50 for x in pomiary)
print(f"czy wszystkie pomiary sa ok? {'tak' if alarmyyyys else 'nie'}")


