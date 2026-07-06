import sys
 
def main():
    # Read M and N from the input line
    m, n = map(int, sys.stdin.readline().split())
    
    # Calculate the maximum number of dominoes using floor division
    max_dominoes = (m * n) // 2
    
    # Output the result
    print(max_dominoes)
 
if __name__ == '__main__':
    main()