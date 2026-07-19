n = input()
lucky_count = sum(1 for c in n if c in "47")
print("YES" if lucky_count in (4, 7) else "NO")734A	Anton and Danik