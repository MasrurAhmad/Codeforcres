import sys

for line in sys.stdin.read().splitlines()[1:]:
    if line:
        a, b = map(int, line.split())
        print(0 if a % b == 0 else b - (a % b))