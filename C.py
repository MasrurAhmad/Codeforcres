def solve():
    y = int(input().strip())
    
    while True:
        y += 1
        if len(set(str(y))) == len(str(y)):
            print(y)
            break

if __name__ == "__main__":
    solve()