def parilliset(lista):
    return [luku for luku in lista if luku % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7]

print("Alkuperäinen:", lista)
print("Parilliset:", parilliset(lista))