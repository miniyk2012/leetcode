import heapq


def merge_sort(l, key=None, reverse=None):
    if len(l) <= 1:
        yield from l
        return
    mid = len(l) // 2
    yield from heapq.merge(merge_sort(l[:mid], key=key, reverse=reverse),
                           merge_sort(l[mid:], key=key, reverse=reverse),
                           key=key, reverse=reverse)


if __name__ == '__main__':
    a = []
    print(list(merge_sort(a)))

    a = [4]
    print(list(merge_sort(a)))

    a = [5, 6, 10, 7, -8, 2, 1, 6]
    print(merge_sort(a))
    print(list(merge_sort(a)))

    print(list(merge_sort(a, reverse=True)))

    print(list(merge_sort(a, key=abs)))

    g = merge_sort(a, key=abs, reverse=True)
    container = []
    while True:
        try:
            container.append(next(g))
        except StopIteration as e:
            print(container)
            break

