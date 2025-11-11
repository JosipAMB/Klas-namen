print("Kies het type procentsom:")
print("1. Percentage van een getal berekenen")
print("2. Hoeveel procent iets is van iets anders")
print("3. Procentuele stijging")
print("4. Procentuele daling")
print("5. Nieuwe waarde na stijging")
print("6. Oude waarde voor stijging")

keuze = int(input("Maak je keuze (1-6): "))

def procent_van_getal():
    getal = float(input("Welk getal? "))
    procent = float(input("Hoeveel procent daarvan? "))
    resultaat = getal * procent / 100
    print(procent, "% van", getal, "=", resultaat)

def hoeveel_procent_van():
    deel = float(input("Welk deel? "))
    geheel = float(input("Van welk geheel? "))
    resultaat = deel / geheel * 100
    print(deel, "is", round(resultaat, 2), "% van", geheel)

def procentuele_stijging():
    oud = float(input("Oude waarde: "))
    nieuw = float(input("Nieuwe waarde: "))
    stijging = (nieuw - oud) / oud * 100
    print("Stijging:", round(stijging, 2), "%")

def procentuele_daling():
    oud = float(input("Oude waarde: "))
    nieuw = float(input("Nieuwe waarde: "))
    daling = (oud - nieuw) / oud * 100
    print("Daling:", round(daling, 2), "%")

def nieuwe_waarde_na_stijging():
    oud = float(input("Oude waarde: "))
    procent = float(input("Stijging in procent: "))
    nieuw = oud * (1 + procent / 100)
    print("Nieuwe waarde =", nieuw)

def oude_waarde_voor_stijging():
    nieuw = float(input("Nieuwe waarde: "))
    procent = float(input("Stijging in procent: "))
    oud = nieuw / (1 + procent / 100)
    print("Oude waarde =", oud)

if keuze == 1:
    procent_van_getal()
elif keuze == 2:
    hoeveel_procent_van()
elif keuze == 3:
    procentuele_stijging()
elif keuze == 4:
    procentuele_daling()
elif keuze == 5:
    nieuwe_waarde_na_stijging()
elif keuze == 6:
    oude_waarde_voor_stijging()
else:
    print("Ongeldige keuze.")

while True:
    print("\nKies het type procentsom:")
    print("1. Percentage van een getal berekenen")
    print("2. Hoeveel procent iets is van iets anders")
    print("3. Procentuele stijging")
    print("4. Procentuele daling")
    print("5. Nieuwe waarde na stijging")
    print("6. Oude waarde voor stijging")
    print("7. Stoppen")

    keuze = int(input("Maak je keuze (1-7): "))

    if keuze == 1:
        procent_van_getal()
    elif keuze == 2:
        hoeveel_procent_van()
    elif keuze == 3:
        procentuele_stijging()
    elif keuze == 4:
        procentuele_daling()
    elif keuze == 5:
        nieuwe_waarde_na_stijging()
    elif keuze == 6:
        oude_waarde_voor_stijging()
    elif keuze == 7:
        print("Programma afgesloten.")
        break
    else:
        print("Ongeldige keuze.")