import sys
 
def solve():
    # Read all inputs from standard input
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    statements = input[1:n+1]
    
    x = 0
    for statement in statements:
        # If '+' is in the statement (e.g., "++X" or "X++"), increment x
        if '+' in statement:
            x += 1
        # Otherwise, it must be '-' (e.g., "--X" or "X--"), decrement x
        else:
            x -= 1
            
    print(x)
 
if __name__ == '__main__':
    solve()