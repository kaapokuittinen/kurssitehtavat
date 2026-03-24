def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    g = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
    if g < 0:
        break
    print(f"{gallonat_litroiksi(g):.2f} litraa")