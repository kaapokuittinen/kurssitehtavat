lista = ["leipä", "maito", "kahvinkeitin", "koira", "ruokakauppa"]

laskuri = 0

for sana in lista:
    if len(sana) > 5:
        laskuri += 1

print("yli 5 kirjainti sisältäviä sanoja: ", laskuri)

