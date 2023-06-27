
import random
import math

p = True

fs = 0

while p:

    rng = math.floor(random.random() * (100 - 1 + 1) + 1)
    probability = 20 + fs
    # print(probability)
    # print(f"rng {rng}")
    print(f"fs = {math.ceil(fs) }")
    print(f"enchantment chance: {probability}%")
    input("")

    if probability > rng:
        fs = 0
        print("item enchanted!")

    if probability < rng:
        fs += 0.75
        print("enchantment failed")

