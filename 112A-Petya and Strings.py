import sys
 
def solve():
    str1 = sys.stdin.readline().strip().lower()
    str2 = sys.stdin.readline().strip().lower()
    
    if str1 < str2:
        print("-1")
    elif str1 > str2:
        print("1")
    else:
        print("0")
 
if __name__ == "__main__":
    solve()
