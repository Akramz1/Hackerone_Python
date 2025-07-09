n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for i in range(commands):
    op = input().split()
    if op[0] == "pop":
        s.pop()
    elif op[0] == "remove":
        s.remove(int(op[1]))
    else:
        s.discard(int(op[1]))
sum = 0
for i in s:
    sum += i
print(sum)
