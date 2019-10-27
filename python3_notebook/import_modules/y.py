from importlib import reload

import x
from x import xo

print(xo.val)
import z

print(z.get_x())
xo.increment()
print(xo.val)
print(z.get_x())

print('after reload')
reload(x)  # 重新加载
print(xo.val)  # 这个是老的xo, 1
print(z.get_x())  # 这个是老的xo, 1

from x import xo
# print(id(xo))
print(xo.val)  # 这个是新的xo, 1
xo.increment()
xo.increment()
xo.increment()
print(xo.val)  # 这个是新的xo, 3
print(z.get_x())  # 这个是老的xo, 1


