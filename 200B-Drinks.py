n = int(input())
percentages = list(map(int, input().split()))
print(f"{sum(percentages) / n:.12f}")