import sys

def solve():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    # s[::-1] creates the reversed copy of string s
    if s[::-1] == t:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()