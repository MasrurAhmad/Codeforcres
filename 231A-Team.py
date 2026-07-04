import sys
 
def solve():
    # Read all input from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
 
    # The first element is the number of problems
    n = int(data[0])
    
    solved_count = 0
    idx = 1
    
    # Iterate through each problem's votes
    for _ in range(n):
        petya = int(data[idx])
        vasya = int(data[idx+1])
        tonya = int(data[idx+2])
        
        # If the sum of confident friends is >= 2, increment the count
        if petya + vasya + tonya >= 2:
            solved_count += 1
            
        idx += 3
        
    print(solved_count)
 
if __name__ == '__main__':
    solve()