# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
s1 = set(map(int, input().split()))
N = int(input())
s2 = set(map(int, input().split()))
ans = sorted(s1.symmetric_difference(s2))
for i in ans:
    print(i)
