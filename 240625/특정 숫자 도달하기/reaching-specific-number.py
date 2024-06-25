arr = list(map(int, input().split()))
bound = 10

for i in range(len(arr)):
    if arr[i] >= 250:
        bound = i
        break

arr = arr[:bound]
total = sum(arr)

print(total, total / len(arr))