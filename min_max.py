def min_max(arr: list) -> tuple:
    if not arr:
        raise ValueError("Array is empty")

    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    mid = len(arr) // 2
    left = min_max(arr[:mid])
    right = min_max(arr[mid:])

    overall_min = left[0] if left[0] < right[0] else right[0]
    overall_max = left[1] if left[1] > right[1] else right[1]

    return overall_min, overall_max


if __name__ == '__main__':
    array = [18, -5, 12, 9, 11, 10, -10, 10, -150]
    min_val, max_val = min_max(array)
    print(f"Min: {min_val}\nMax: {max_val}")
