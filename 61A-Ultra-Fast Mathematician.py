s1, s2 = input(), input()
print("".join('1' if a != b else '0' for a, b in zip(s1, s2)))