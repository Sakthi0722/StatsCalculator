import random


def simple_random_Sampling(data):
    try:
        sampled_list = random.sample(data, 15)
        print("Sample data :", sampled_list)
        return sampled_list
    except ValueError:
        print("ERROR: Check your input value")
