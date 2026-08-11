n = int(input())
levels = set(map(int, input().split()[1:])) | set(map(int, input().split()[1:]))
if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")