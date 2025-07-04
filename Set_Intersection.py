# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
num1 = set(map(int, input().split()))
M = int(input())
num2 = set(map(int, input().split()))
print(len(num1 & num2))
