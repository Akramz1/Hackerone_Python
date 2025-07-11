# Enter your code here. Read input from STDIN. Print output to STDOUT
# import calendar
import calendar
s = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(s[2], s[0], s[1])].upper())
