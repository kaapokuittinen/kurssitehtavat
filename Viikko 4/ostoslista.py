ostoslista = ["maito", "leipä", "kurkku", "jauheliha", "karkki", "rahka"]

ostos = input("Anna tuote: ")

while ostos in ostoslista:
    ostoslista.remove(ostos)
    print(ostoslista)
    print(f"{ostos} poistettu listalta")
    ostos = input("Anna tuote: ")
else:
    print(f"{ostos} ei ole listalla")

