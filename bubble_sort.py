def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] < arr[j + 1]:  # ❌ Wrong comparison — sorts descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# Expected: [11, 12, 22, 25, 34, 64, 90]
