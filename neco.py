muj_list = [
    "Ostrava",
    "Kladno",
    "Praha",
    "Liberec",
    "Opava",
    "České Budějovice",
    "Litoměřice"
]

vstup = int(input("Zadejte index města: "))

# Cvičení 3: Váš kód sem 👇

if 0 <= vstup < len(muj_list):
    
    for index, mesto in enumerate(muj_list):
        if index == vstup:
            print("vybrano")
        else:
            print(index, mesto)
else:
    print("chybny vstup")