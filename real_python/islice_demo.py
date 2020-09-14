def count(n):
    while True:
        yield n
        n += 1


c = count(0)
import itertools

for x in itertools.islice(c, 10, 20):
    print(x)

print()
items = ['a', 'b', 'c', 1, 4, 10, 15, 'e']
for x in itertools.islice(items, 3, None):
    print(x)
print()
for x in itertools.dropwhile(lambda x: isinstance(x, str), items):
    print(x)
