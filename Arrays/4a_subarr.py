# Subarray sum equals k
# Sliding Window works only for +ve nums in the array

# Brute Force only for +ve nums
def subarraySum(arr, n, k):
    low = 0 
    high = 0
    cnt = 0
    currSum = 0

    while high < n:
        currSum += arr[high]
        while low < high and currSum > k:
            currSum -= arr[low]
            low += 1
        
        if currSum == k:
            cnt += 1
        high += 1
    
    return cnt




# Both +ve and -ve nums
# Brute Force
def subarraySum(arr, n, k):
    cnt = 0
    currSum = 0
    for i in range(n):
        currSum = arr[i]
        if currSum == k:
            cnt += 1
        
        for j in range(i + 1, n):
            currSum += arr[j]
            if currSum == k:
                cnt += 1
    
    return cnt




# Using map
def subarraySum(arr, n, k):
    map = {}
    currSum = 0
    cnt = 0
    map[0] = 1

    for i in range(n):
        currSum += arr[i]
        rem = currSum - k
        if rem in map:
            cnt += map[rem]
        if currSum in map:
            map[currSum] += 1
        else:
            map[currSum] = 1
    
    return cnt


