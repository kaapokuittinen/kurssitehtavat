<<<<<<< HEAD
pituus = float(input("Kuhan pituus senttimetreinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
=======
pituus = float(input("Kuhan pituus senttimetreinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
>>>>>>> 9863bc1ec262abbdbd13812c4ed8dd8d00c78803
    print("Kuha on sallittua pyyntimittaa.")