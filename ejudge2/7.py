a=int(input())
b=[int(x) for x in input().split()]
max=-100000000000000
index=0
for i in range(b):
    if b[i]>max:
        max=b[i]
        index=i+1
print(index)