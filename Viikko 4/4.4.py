import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Arvaa luku (1-10): "))

    if guess < secret:
        print("Liian pieni arvaus")
    elif guess > secret:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break