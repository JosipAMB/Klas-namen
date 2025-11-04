def procent_van_getal():
    getal = float(input("Welk getal? "))
    procent = float(input("Hoeveel procent daarvan? "))
    resultaat = getal * procent / 100
    print(f"{procent}% van {getal} = {resultaat}")

def hoeveel_procent_van():
    deel = float(input("Welk deel? "))
    geheel = float(input("Van welk geheel? "))
    resultaat = deel / geheel * 100
    print(f"{deel} is {resultaat:.2f}% van {geheel}")

def procentuele_stijging():
    oud = float(input("Oude waarde: "))
    nieuw = float(input("Nieuwe waarde: "))
    stijging = (nieuw - oud) / oud * 100
    print(f"Stijging: {stijging:.2f}%")

def procentuele_daling():
    oud = float(input("Oude waarde: "))
    nieuw = float(input("Nieuwe waarde: "))
    daling = (oud - nieuw) / oud * 100
    print(f"Daling: {daling:.2f}%")

def nieuwe_waarde_na_stijging():
    oud = float(input("Oude waarde: "))
    procent = float(input("Stijging in procent: "))
    nieuw = oud * (1 + procent / 100)
    print(f"Nieuwe waarde = {nieuw}")

def oude_waarde_voor_stijging():
    nieuw = float(input("Nieuwe waarde: "))
    procent = float(input("Stijging in procent: "))
    oud = nieuw / (1 + procent / 100)
    print(f"Oude waarde = {oud}")

def main():
    print("Kies het type procentsom:")
    print("1. Percentage van een getal berekenen")
    print("2. Hoeveel procent iets is van iets anders")
    print("3. Procentuele stijging")
    print("4. Procentuele daling")
    print("5. Nieuwe waarde na stijging")
    print("6. Oude waarde vóór stijging")
    
    keuze = int(input("Maak je keuze (1-6): "))

    match keuze:
        case 1:
            procent_van_getal()
        case 2:
            hoeveel_procent_van()
        case 3:
            procentuele_stijging()
        case 4:
            procentuele_daling()
        case 5:
            nieuwe_waarde_na_stijging()
        case 6:
            oude_waarde_voor_stijging()
        case _:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()