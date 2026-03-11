import random

N = int(input("Kuinka monta pistettä arvotaan? "))
inside = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        inside += 1

pi_estimate = 4 * inside / N

print("Piin likiarvo:", pi_estimate)