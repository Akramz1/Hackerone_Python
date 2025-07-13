# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = float(input())
bc = float(input())
r = math.atan2(ab, bc)
d = math.degrees(r)
print(int(round(d)), chr(176), sep="")
