n = int(input())
ans = 0
for bill in (100, 20, 10, 5, 1):
    ans += n // bill
    n %= bill
print(ans)