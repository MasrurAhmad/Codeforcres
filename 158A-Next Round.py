import sys

def solve():
    # Read n and k
    n, k = map(int, sys.stdin.readline().split())
    
    # Read the scores list
    scores = list(map(int, sys.stdin.readline().split()))
    
    # Identify the threshold score (k-th place finisher)
    # Using k-1 because Python lists are 0-indexed
    threshold_score = scores[k - 1]
    
    count = 0
    for score in scores:
        # A participant advances if they meet or beat the threshold AND have a positive score
        if score >= threshold_score and score > 0:
            count += 1
        else:
            # Since the array is sorted in descending order, if this participant 
            # doesn't qualify, none of the remaining ones will either.
            break
            
    print(count)

if __name__ == '__main__':
    solve()