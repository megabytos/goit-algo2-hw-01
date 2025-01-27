def kth_smallest(arr: list, k: int) -> int | float:
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]

    left, right, pivots = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            pivots.append(num)

    if k <= len(left):
        return kth_smallest(left, k)
    elif k > len(left) + len(pivots):
        return kth_smallest(right, k - len(left) - len(pivots))
    else:
        return pivots[0]


if __name__ == '__main__':
    k = 3
    array = [138, -5, 12, 66, 11, -4, -20, 10, -80, -5, 11, 66, 18, -14, -20, 6, -10, 5, -7, 9, 45, -13, 28, 0, -15, 22, 4, 16, 8, -10, 12, 14, 1, 18, 20]
    elem = kth_smallest(array, k)
    print(f'{k}-th smallest: {elem}')
