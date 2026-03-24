# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:
cislo = float(input("Zadej číslo: "))
cislo += 10
print("Výsledek:", cislo)
# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():
ucet = float(input("Zadej celkovou částku: "))
lidi = int(input("Zadej počet lidí: "))
na_osobu = ucet / lidi
print(f"Každý zaplatí {na_osobu:.2f} Kč")
# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
# plocha = 3.14 * r * r
# Sem doplň kód:
r = float(input("Zadej poloměr: "))
plocha = 3.14 * r ** 2
print("Plocha kruhu je:", round(plocha))
