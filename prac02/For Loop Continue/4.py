a=[int(x) for x in input().split()]
b=int(input())
c=int(input())
for x in a:
    if x>b and x<c:
        continue
    print(x+b+c)