import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    h = int(data[1])
    heights = [int(x) for x in data[2:]]

    total_width = sum(2 if a > h else 1 for a in heights)
    print(total_width)

if __name__ == '__main__':
    solve()