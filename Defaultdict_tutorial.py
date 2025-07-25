# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())
a = defaultdict(list)
b = defaultdict(list)
for _ in range(n):
    a['a'].append(input())
for _ in range(m):
    b['b'].append(input())

for i in b['b']:
    pos = [j+1 for j, val in enumerate(a['a']) if i==val]
    if pos:
        print(*pos)
    else:
        print('-1')