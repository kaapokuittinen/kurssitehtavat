import math
leiviska = float(input("Anna leiviskät.\n"))
naula = float(input("Anna naulat.\n"))
luoti = float(input("Anna luodit.\n"))
leiviska = leiviska*20*32
naula = naula*32
massa_nykymittojen_mukaan = (leiviska+naula+luoti)*13.3
kilogrammaa = int(massa_nykymittojen_mukaan // 1000)
grammaa = massa_nykymittojen_mukaan % 1000

print(f"Massa nykymittojen mukaan: {kilogrammaa} kilogrammaa ja {grammaa:.2f} grammaa")