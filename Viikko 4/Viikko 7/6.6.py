import math

def pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m**2
    return hinta_euro / pinta_ala

d1 = float(input("Pizza 1 halkaisija (cm): "))
h1 = float(input("Pizza 1 hinta (€): "))

d2 = float(input("Pizza 2 halkaisija (cm): "))
h2 = float(input("Pizza 2 hinta (€): "))

y1 = pizzan_yksikkohinta(d1, h1)
y2 = pizzan_yksikkohinta(d2, h2)

print(f"Pizza 1: {y1:.2f} €/m²")
print(f"Pizza 2: {y2:.2f} €/m²")

if y1 < y2:
    print("Pizza 1 on parempi valinta.")
else:
    print("Pizza 2 on parempi valinta.")