import random

l1 = [2, 4, 6, 8, 5, 7]

n = 3

for i in range(n):
    random.seed(1)
    r1 = random.choice(l1)
    print("Select N number of items from a list with a seed:", r1)
