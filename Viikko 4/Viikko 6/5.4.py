kaupungit = []

for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

print("Kaupungit järjestyksessä:")
for kaupunki in kaupungit:
    print(kaupunki)