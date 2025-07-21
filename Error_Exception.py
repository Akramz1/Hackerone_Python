# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except (ValueError,ZeroDivisionError) as e:
        print("Error Code:",e)