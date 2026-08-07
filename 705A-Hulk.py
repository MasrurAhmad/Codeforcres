n = int(input())
layers = ["I hate" if i % 2 == 1 else "I love" for i in range(1, n + 1)]
print(" that ".join(layers) + " it")