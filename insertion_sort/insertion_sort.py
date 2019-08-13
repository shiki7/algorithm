def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        if tmp < arr[i - 1]:
            j = i
            while True:
                arr[j] = arr[j - 1]
                j -= 1
                if j == 0 or tmp > arr[j - 1]:
                    break
            arr[j] = tmp
    return arr

# デバック
if __name__ == "__main__":
    arr = [3, 4, 6, 10, 2, 1, 7, 11]
    print("before: ", arr)
    arr = insertion_sort(arr)
    print("after: ", arr)
