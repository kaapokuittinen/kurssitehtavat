def inventaario(tavarat):
    print("Repussasi on: ")
    for t in tavarat:
        print("-",t)
    tavarat.clear()

    return

#Pääohjelma
reppu = ["juomapullo", "kynä", "avaimet"]
inventaario(reppu)
reppu.append("eväsleipä")
inventaario(reppu)
