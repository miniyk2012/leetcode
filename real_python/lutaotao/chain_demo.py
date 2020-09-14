from itertools import chain

a = [1, 2, 3, 4]
b = set(['a', 'b', 'c', 'd'])
for x in chain(a, b):
    print(x)
