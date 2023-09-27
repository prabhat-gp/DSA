# 189. Rotate Array(Left and Right) 
# Rotate the array to right by k steps
def solve(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

# Rotate Right
def rotateRight(arr, n, k):
    if k % n == 0:
        return
    k = k % n

    solve(arr, 0, n - k - 1)
    solve(arr, n - k, n - 1)
    solve(arr, 0, n - 1)
    return arr


# Rotate Left
def rotateLeft(arr, n, k):
    if k % n == 0:
        return
    k = k % n

    solve(arr, 0, k - 1)
    solve(arr, k, n - 1)
    solve(arr, 0, n - 1)
    return arr
