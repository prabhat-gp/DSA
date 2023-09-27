# Number of Arithmetic Triplets (2367)

# Brute Force
def arithmeticTriplets(arr, diff):
    n = len(arr)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[j] - arr[i] == diff and arr[k] - arr[j] == diff:
                    cnt += 1

    return cnt



# Optimal
def arithmeticTriplets(arr, diff):
    n = len(arr)
    cnt = 0

    for i in range(n): 
        low = i + 1
        high = n - 1
        while low < high:
            temp1 = arr[low] - arr[i]
            temp2 = arr[high] - arr[low]
            if temp1 == diff and temp2 == diff:
                cnt += 1
                low += 1
                high -= 1
            elif temp1 < diff or temp2 < diff:
                low += 1
            else:
                high -= 1
        
    return cnt



# Number of Unequal Triplets in an Array (2475)
def unequalTriplets(arr):
    n = len(arr)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] != arr[j] and arr[j] != arr[k] and arr[k] != arr[i]:
                    cnt += 1

    return cnt