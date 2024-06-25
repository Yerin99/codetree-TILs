n = int(input())
grades = list(map(float, input().split()))
gpa = round(sum(grades) / n, 1)
print(gpa)

if gpa >= 4.0:
    print("Perfect")
elif gpa >= 3.0:
    print("Good")
else:
    print("Poor")