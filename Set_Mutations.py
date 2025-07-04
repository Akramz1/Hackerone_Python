# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
se = set(map(int, input().split()))
op = int(input())
for i in range(op):
    s1 = input().split()
    if s1[0] == "intersection_update":
        getin = map(int, input().split())
        se.intersection_update(getin)
        print
    elif s1[0] == 'update':
        getin = set(map(int, input().split()))
        se |= getin
    elif s1[0] == 'difference_update':
        getin = set(map(int, input().split()))
        se -= getin
    else:
        getin = set(map(int, input().split()))
        se ^= getin
summation = 0
for i in se:
    summation += i
print(summation)
