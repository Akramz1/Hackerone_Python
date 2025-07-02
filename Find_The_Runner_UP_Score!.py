n = int(input())
arr = list(map(int, input().split()))
mx = -100
mx2 = -100
for i in arr:
    if i > mx:
        mx = i
for i in arr:
    if i > mx2 and i != mx:
        mx2 = i
print(mx2)
