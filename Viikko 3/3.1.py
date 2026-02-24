pituus = float(input("Kuhan pituus senttimetreinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallittua pyyntimittaa.")