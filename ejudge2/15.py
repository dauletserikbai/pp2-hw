a = int(input())
unq = set()

for i in range(a):
    x = input().strip()
    unq.add(x)
print(len(unq))