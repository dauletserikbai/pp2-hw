a=int(input())
b=[int(x) for x in input().split()]
mx=-10**9
mn=10**9
for i in range(len(b)):
    if b[i]>mx:
        mx=b[i]
    if b[i]<mn:
        mn=b[i]
for i in range(len(b)):
    if b[i]==mx:
        b[i]=mn
for i in b:
    print(i, end=" ")

