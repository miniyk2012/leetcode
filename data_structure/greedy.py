money = [20, 10, 5, 1]


def cents_36(cents):
    ret = {}
    for cent in money:
        num, cents = divmod(cents, cent)
        ret[cent] = num
    print(ret)


if __name__ == '__main__':
    cents_36(36)
    cents_36(138)
