import matplotlib.pyplot as plt

liczba_studentow = int(input("Podaj liczbę studentów: "))

nazwiska = []
punkty = []
oceny = []

for i in range(liczba_studentow):
  print(f"\nStudent {i+1}:")
  nazwisko = input("Podaj nazwisko: ")
  
  while True:
    pkt = float(input("Podaj wynik punktowy (0-100): "))
    if 0 <= pkt <= 100:
      break
    print("Błędna wartość! Liczba punktów musi być w zakresie od 0 do 100.")

  if pkt <= 49:
    ocena = 2.0
  elif pkt <= 59:
    ocena = 3.0
  elif pkt <= 69:
    ocena = 3.5
  elif pkt <= 79:
    ocena = 4.0
  elif pkt <= 89:
    ocena = 4.5
  else:
    ocena = 5.0

  nazwiska.append(nazwisko)
  punkty.append(pkt)
  oceny.append(ocena)

srednia_ocen = sum(oceny) / len(oceny) if len(oceny) > 0 else 0
liczba_zaliczonych = sum(1 for o in oceny if o >= 3.0)

print("\n--- PODSUMOWANIE WYNIKÓW ---")
for n, p, o in zip(nazwiska, punkty, oceny):
  print(f"Student: {n} | Punkty: {p} | Ocena: {o}")

print(f"\nŚrednia ocen wszystkich studentów: {srednia_ocen:.2f}")
print(f"Liczba studentów z oceną co najmniej 3.0: {liczba_zaliczonych}")

plt.figure(figsize=(10, 6))
plt.bar(nazwiska, oceny, color='skyblue', edgecolor='black')

plt.title("Analiza ocen studentów z egzaminu", fontsize=14)
plt.xlabel("Nazwiska studentów", fontsize=12)
plt.ylabel("Oceny", fontsize=12)

plt.yticks([2.0, 3.0, 3.5, 4.0, 4.5, 5.0])
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()