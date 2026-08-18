for _ in range(int(input())):
    s = input()
    ans = [c + "0" * (len(s) - 1 - i) for i, c in enumerate(s) if c != "0"]
    print(len(ans))
    print(*ans)