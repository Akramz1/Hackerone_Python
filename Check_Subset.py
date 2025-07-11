# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
while T != 0:
    flag = True
    N = int(input())
    s1 = set(map(int, input().split()))
    N2 = int(input())
    s2 = set(map(int, input().split()))
    for i in s1:
        if i not in s2:
            flag = False
            break
    print(flag)
    T -= 1
