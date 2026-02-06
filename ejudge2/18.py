a=int(input())
b={}
for i in range(a):
    x = input().strip()
    if x not in b:
        b[x] = i + 1
for x in sorted(b):
    print(x, b[x])