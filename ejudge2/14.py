a=int(input())
b=[int(x) for x in input().split()]
dc={}
for x in b:
    if x in dc:
        dc[x]+=1
    else:
        dc[x]=1
ans=0
mx=0
for x in b:
    if dc[x]>mx or (mx==dc[x] and x<ans):
        mx=dc[x]
        ans=x
print(ans)