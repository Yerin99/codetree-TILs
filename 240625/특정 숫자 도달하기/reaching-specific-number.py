arr = list(map(int, input().split()))
n = len(arr)
bound = 9

for i in range(n):
    if arr[i] >= 250:
        bound = i
        break

total = sum(arr[:bound])

print(total, total / bound)