# ÚLOHA 1: Sčítací past (Cíl: 5 + 3 = 8)
# ---------------------------------------------------------
cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))
print("Součet je:", cislo1 + cislo2)
# ÚLOHA 2: Opakovač jména (Cíl: "Honza" a 3 -> "HonzaHonzaHonza")
# ---------------------------------------------------------
jmeno = input("Zadej jméno: ")
pocet = int(input("Kolikrát se má jméno opakovat: "))
print(jmeno * pocet)
# ÚLOHA 3: Rok narození (Cíl: 2026 - věk)
# ---------------------------------------------------------
vek = int(input("Kolik ti je let: "))
rok_narozeni = 2026 - vek
print(f"Narodil ses přibližně v roce {rok_narozeni}")
# ÚLOHA 4: Výplata (Cíl: mzda * hodiny)
# ---------------------------------------------------------
mzda = int(input("Zadej hodinovou mzdu: "))
hodiny = int(input("Zadej počet hodin: "))
vyplata = mzda * hodiny
print(f"Celková odměna je: {vyplata}")
# ÚLOHA 5: Magická matematika (Cíl: (x + 10) * 2)
# ---------------------------------------------------------
cislo = int(input("Zadej číslo: "))
vysledek = (cislo + 10) * 2
print(f"Výsledek je: {vysledek}")
