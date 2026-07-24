import sys


def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    n = int(data[0])
    opinions = data[1:]

    if "1" in opinions:
        print("HARD")
    else:
        print("EASY")


if __name__ == "__main__":
    solve()