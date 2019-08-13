def select_sort(arr):
    for i in range(len(arr)):
        min_val = min(arr[i:])
        min_idx = arr.index(min_val)
        arr[i], arr[min_idx] = min_val, arr[i]
    return arr


# デバック
if __name__ == "__main__":
    arr = [3, 4, 6, 10, 2, 1, 7, 11]
    print("before: ", arr)
    arr = select_sort(arr)
    print("after: ", arr)
