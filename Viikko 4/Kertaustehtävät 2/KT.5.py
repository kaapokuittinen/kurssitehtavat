def suurin_arvo(yks, kaks, kolme):
    return max(yks, kaks, kolme)

luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luku3 = int(input("Anna kolmas luku: "))

print("Suurin arvo on: ", suurin_arvo(luku1, luku2, luku3))
