n = int(input())
p = list(map(int, input().split()))
ans = [0] * (n + 1)

for i in range(1, n + 1):
    ans[p[i - 1]] = i

print(*ans[1:])