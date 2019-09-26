import sys

print(sys.getsizeof([]))

x = []
x.append(4)
x.append(4)
x.append(4)
z = [7, 70, {'10': 10}]
print(sys.getsizeof(x))
print(sys.getsizeof(z))
x.pop()
x.pop()
x.pop()

print(sys.getsizeof(x))
y = [8]
print(sys.getsizeof(y))
while y:
    y.pop()
print(sys.getsizeof(y))
