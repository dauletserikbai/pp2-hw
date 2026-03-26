names = ["Фархат", "Ардак", "Куаныш"]
scores = [75, 98, 65]

for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)