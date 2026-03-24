def vaihda_nimi():
    kaupunki = "Vantaa"     #lokaali muuttuja
    print("Funktion päätyessä kaupunki on", kaupunki)
    return

#Pääohjelma
kaupunki = "Helsinki"       #globaali muuttuja
print("Ennen funktiokutsua kaupunki on", kaupunki)
vaihda_nimi()
print("Funktiokutsun jälkeen kaupunki on", kaupunki)