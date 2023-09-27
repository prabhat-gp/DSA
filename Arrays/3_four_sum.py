# 4 Sum (18)

# Brute Force
def fourSum(arr, target):
    arr.sort()
    s = set()
    n = len(arr)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    sum = arr[i] + arr[j] + arr[k] + arr[l]
                    if sum == target:
                        s.add((arr[i], arr[j], arr[k], arr[l]))
        
    temp = []
    for nums in s:
        temp.append(nums)

    return temp


# Better Solution
def fourSum(arr, k):
    arr.sort()
    s = set()
    n = len(arr)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            target = k - arr[i] - arr[j]
            low = j + 1
            high = n - 1
            while low < high:
                sum = arr[i] + arr[j] + arr[low] + arr[high]
                if sum == k:
                    s.add((arr[i], arr[j], arr[low], arr[high]))
                    low += 1
                    high -= 1
                if arr[low] + arr[high] < target:
                    low += 1
                elif arr[low] + arr[high] > target:
                    high -=1
        
    temp = []
    for nums in s:
        temp.append(nums)
        
    return temp
                



# Count Special Quadruplets (1995)

def countQuadruplets(arr):
    ans = 0
    n = len(arr)
    map = {
        (arr[0] + arr[1] + arr[2]): 1
    }

    for i in range(3, n):
        ans += map.get(arr[i], 0)
        for j in range(i - 1):
            for k in range(j + 1, i):
                sum = arr[i] + arr[j] + arr[k]
                map[sum] = map.get(sum, 0) + 1
    return ans

    