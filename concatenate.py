# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,m,p = map(int,(input()).split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1+= map(int,(input()).split())
for _ in range(m):
    arr2+= map(int,(input()).split())
output = np.concatenate((arr1,arr2))
output.shape = (n+m,p)
print(output)