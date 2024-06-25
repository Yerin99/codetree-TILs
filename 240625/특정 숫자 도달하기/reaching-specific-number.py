arr = list(map(int, input().split()))
bound = 10

for i in range(9):
    if arr[i] >= 250:
        bound = i
        break

arr = arr[:bound]
total = sum(arr)

print(total, total / len(arr))