# === Vytvoření souboru (NEMĚNIT) ===
from datetime import date

with open("osoby.txt", "w") as soubor:
    soubor.write("Petr 1990-08-28\n")
    soubor.write("Jana 1985-05-20\n")
    soubor.write("Pavel 2001-12-10\n")
    soubor.write("Lucie 1978-03-08\n")
    soubor.write("Martin 1995-07-25\n")

# Váš kód sem 👇

dnes = date.today() # dnešní datum získáme pomocí knihovny datetime

with open('osoby.txt', 'r') as s:
  for radek in s: # for cyklem čteme soubor řádek po řádku až dokonce souboru

    data = radek.strip().split() # strip() odstraní bílé znaky ze začátku a konce textu, split() rozdělí text v místech, kde jsou mezery
    jmeno = data[0] # první část textu je jméno
    datum_narozeni = data[1] # druhá část textu je datum narození
    rok, mesic, den = map(int, datum_narozeni.split('-')) # split() rozdělí datum v místech, kde jsou pomlčky, map() převede každou část na integer (celé číslo)

    if date(dnes.year, mesic, den) == dnes: # ze tří integerů (celých čísel) vytvoříme skutečné "datum" (nikoliv jen text), které se umí porovnat s jiným datumem
      print(f"Blahopřeji k narozeninám, {jmeno}!")
