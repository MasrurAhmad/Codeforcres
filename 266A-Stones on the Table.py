_, s = open(0).read().split()
print(sum(a == b for a, b in zip(s, s[1:])))