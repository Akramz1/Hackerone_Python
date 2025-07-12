# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
shoes = list(map(int, input().split()))
N = int(input())
count = 0
for i in range(N):
    x = input().split()
    if int(x[0]) in shoes:
        count += int(x[1])
        shoes.remove(int(x[0]))
print(count)
