a=int(input())
b=[2**int(x) for x in input().split()]
if a in b:
    print("YES")
else:
    print("NO")