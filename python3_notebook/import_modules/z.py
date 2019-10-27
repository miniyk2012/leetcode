from x import xo
import x


def get_x():
    print(id(xo), id(x.xo))
    print('x', x.xo.val)  # 新的模块的值
    return xo.val  # 旧的值
