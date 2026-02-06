a=int(input())
b=[x for x in range(1, a+1)]
c=0
for i in b:
    if a%i==0:
        c+=1
if c==2:
    print("Yes")
else:
    print("No")