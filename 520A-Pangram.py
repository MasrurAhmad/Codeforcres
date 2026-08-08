n = int(input())
s = input().strip()

print("YES" if len(set(s.lower())) == 26 else "NO")