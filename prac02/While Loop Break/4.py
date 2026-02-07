x=[int(i) for i in input().split()]
b=0
while b<len(x):
    if x[b]%2==0:
        break
    print(x[b])
    b+=1
    