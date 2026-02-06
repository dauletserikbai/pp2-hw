a=int(input())
b=[int(x) for x in input().split()]
max=-100000000000000
for i in range(b):
    if b[i]>max:
        max=b[i]
print(max)

