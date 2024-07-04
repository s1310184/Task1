import random

print("Tossing a coin...")

heads_count = 0
tails_count = 0

for round in range(1, 4):
    result = random.choice(["Heads", "Tails"])
    print(f"Round {round}: {result}")
    
    if result == "Heads":
        heads_count += 1
    else:
        tails_count += 1

print(f"Heads: {heads_count}, Tails: {tails_count}")