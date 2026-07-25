import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    t = int(data[1])
    s = list(data[2])

    for _ in range(t):
        i = 0
        while i < n - 1:
            if s[i] == "B" and s[i + 1] == "G":
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 1  # Skip next index
            i += 1

    print("".join(s))


if __name__ == "__main__":
    solve()