# Equilibrium Point (Pivot Index) (Middle Index)

# Approach 1
def equilibriumPoint(arr, n):
    totalSum = sum(arr)
    leftSum = 0
    for i in range(n):
        if leftSum == totalSum - leftSum - arr[i]:
            return i + 1
        leftSum += arr[i]
    return -1


# Approach 2
def pivotIndex(arr, n):
    totalSum = sum(arr)
    leftSum = 0

    for i in range(n):
        if leftSum * 2 == totalSum - arr[i]:
            return i
        leftSum += arr[i]
    
    return -1


# Prefix Sum
def pivotIndex(arr, n):
    preSum = [0] * n
    preSum[0] = arr[0]

    for i in range(1, n):
        preSum[i] = preSum[i - 1] + arr[i]
        
    for i in range(n):
        if preSum[i] - arr[i] == preSum[n - 1] - preSum[i]:
            return i
        
    return -1