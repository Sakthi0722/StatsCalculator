import random

random.seed(20)
r3 = random.randint(1, 40)

print("Generate a random number with a seed between a range of two numbers - Integer:", r3)

random.seed(20)
r4 = random.uniform(1, 40)

print("Generate a random number with a seed between a range of two numbers - Decimal:", r4)
