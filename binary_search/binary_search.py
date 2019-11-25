def binary_search(list, item):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            left = mid -1
        else:
            right = mid + 1

    return None
