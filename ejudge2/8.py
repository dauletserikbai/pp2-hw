a=int(input())
b=[2**int(x) for x in input().split()]
for i in b:
    if a>=i:
        print(i, end=" ")