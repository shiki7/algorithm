def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr

# デバック
if __name__ == "__main__":
    arr = [3, 4, 6, 10, 2, 1, 7, 11]
    print("before: ", arr)
    arr = bubble_sort(arr)
    print("after: ", arr)
