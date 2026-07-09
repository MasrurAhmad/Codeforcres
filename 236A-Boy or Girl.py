def solve():
    username = input().strip()
    
    distinct_chars = set(username)
    
    if len(distinct_chars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
 
if __name__ == "__main__":
    solve()