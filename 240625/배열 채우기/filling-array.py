arr = list(map(int, input().split()))
bound = 10

if arr.count(0) != 0:
    bound = arr.index(0)

for e in arr[:bound][::-1]:
    print(e, end=" ")