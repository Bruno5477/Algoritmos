def selection_sort(arr:list) -> list:
    n = len(arr)
    for i in range(n - 1):
        j_min = i
        for j in range(i, n):
            if arr[j] < arr[j_min]:
                j_min = j
        if arr[j_min] < arr[i]:
            arr[j_min], arr[i] = arr[i], arr[j_min]
    return arr
