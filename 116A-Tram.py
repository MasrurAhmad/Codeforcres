import sys


def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    n = int(data[0])

    current_passengers = 0
    max_capacity = 0

    idx = 1
    for _ in range(n):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2

        current_passengers -= a
        current_passengers += b

        if current_passengers > max_capacity:
            max_capacity = current_passengers

    print(max_capacity)


if __name__ == "__main__":
    solve()