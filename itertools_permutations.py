# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s = input().split()
perms = (permutations(s[0], int(s[1])))
perms = sorted(perms)
for i in perms:
    print(''.join(i))
