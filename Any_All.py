# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums = list(map(int, (input().split())))
if all(_>0 for _ in nums) and any(str(_) == str(_)[::-1] for _ in nums):
    print("True")
else:
    print("False")