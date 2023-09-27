# Continous Subarray Sum

def checkSubarraySum(arr, n, k):
    map = {}
    map[0] = 0
    currSum = 0
    index = 0

    for i in range(n):
        currSum += arr[i]
        if k != 0:
            currSum = currSum % k

        if currSum not in map:
            map[currSum] = index + 1
        else:
            if map[currSum] < index:
                return True
        
        index += 1
    
    return False
