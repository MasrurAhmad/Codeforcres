k, l, m, n, d = [int(input()) for _ in range(5)]
print(sum(1 for i in range(1, d + 1) if any(i % x == 0 for x in (k, l, m, n))))