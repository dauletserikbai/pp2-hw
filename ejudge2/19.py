a = int(input())
b = {}
for i in range(a):
    name, num = input().split()
    k = int(num)
    if name in b:
        b[name] += k
    else:
        b[name] = k
for x in sorted(b):
    print(x, b[x])