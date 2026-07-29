import sys

m = sys.stdin.read().split()[1:]
print(sum(1 for i in range(1, len(m)) if m[i] != m[i - 1]) + 1 if m else 0)