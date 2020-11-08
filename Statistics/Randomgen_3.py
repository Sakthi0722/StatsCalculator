import random

randomInt = []
for i in range(1, 15):
    random.seed(i)
    x = random.randint(0, 20)
    randomInt.append(x)
print("Generate a list of N random numbers with a seed and between a range of numbers - Integer : ", randomInt)

randomDec = []
for i in range(1, 15):
    random.seed(i)
    x = random.uniform(0, 20)
    randomDec.append(x)
print("Generate a list of N random numbers with a seed and between a range of numbers - Decimals : ", randomDec)

