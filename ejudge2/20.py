a = int(input())

ava ={}
for i in range(a):
    x = input().split()
    if x[0] == "set":
        key = x[1]
        value = x[2]
        ava[key] = value
    elif x[0] == "get":
        key = x[1]
        if key in ava:
            print(ava[key])
        else:
            print(f"KE: no key {key} found in the document")