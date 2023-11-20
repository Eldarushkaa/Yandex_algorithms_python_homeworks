a = int(input())
b = int(input())
n = int(input())
t = 0
if b % n:
    t = 1
if a > b // n + t:
    print("Yes")
else:
    print("No")
