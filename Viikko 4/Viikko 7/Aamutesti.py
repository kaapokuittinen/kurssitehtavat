
hedelmat = {"OMENA": 1, "PÄÄRYNÄ": 2, "BANAANI": 3}
hedelma = input("Hedelmän nimi? : ").upper()

yhteishinta = 0

while True:
    hedelma = input("Hedelmän nimi? : ").upper()

    if hedelma in hedelmat:
         print(f"{hedelma} hinta {hedelmat[hedelma]} €")
         yhteishinta += hedelmat[hedelma]
    else:
        print("Hedelma ei ole tilattavissa")

    if hedelma =="":
        print("Tilaus päättyy...")
        break

    print(yhteishinta)
