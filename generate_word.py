import random


def generate_word():
    with open("sowpods.txt", "r") as f:
        words = list(f)

    f.close()

    return words[random.randint(0, len(words))]
