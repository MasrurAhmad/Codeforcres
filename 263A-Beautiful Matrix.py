import sys

def solve():
    # Read all 5 rows of the matrix
    for r in range(1, 6):
        row = list(map(int, sys.stdin.readline().split()))
        
        # Check if the '1' is in the current row
        if 1 in row:
            # Find the 1-indexed column position
            c = row.index(1) + 1
            
            # Calculate Manhattan distance to (3, 3)
            moves = abs(r - 3) + abs(c - 3)
            print(moves)
            return

if __name__ == '__main__':
    solve()