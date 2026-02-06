a = int(input())
b = {}

for i in range(a):
    x = input().strip()
    b[x] = b.get(x, 0) + 1
l = 0
for i in b:
    if b[i] == 3:
        l += 1
print(l)