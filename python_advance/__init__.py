"""极客时间python核心技术与实战"""


def quick_sort(a):
    if a is None or len(a) == 0:
        return a
    pivot = a[0]
    remain = a[1:]
    left = list(filter(lambda e: e <= pivot, remain))
    right = list(filter(lambda e: e > pivot, remain))
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([4, 10, 6]))
print(quick_sort([4, 4, 6, 7, 8]))
print(quick_sort([4]))
print(quick_sort([]))
