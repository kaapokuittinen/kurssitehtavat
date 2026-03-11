<<<<<<< HEAD
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hb = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

else:
=======
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hb = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

else:
>>>>>>> 9863bc1ec262abbdbd13812c4ed8dd8d00c78803
    print("Virheellinen sukupuoli.")