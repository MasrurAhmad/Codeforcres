n = int(input())
a = list(map(int, input().split()))

mx, mn = a.index(max(a)), len(a) - 1 - a[::-1].index(min(a))
print(mx + (n - 1 - mn) - (1 if mx > mn else 0))