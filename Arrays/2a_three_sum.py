# Three Sum (15)

# Brute Force
def threeSum(arr):
    arr.sort()
    n = len(arr)
    s = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum = arr[i] + arr[j] + arr[k]
                if sum == 0 and i != j and j != k and k != i:
                    s.add((arr[i], arr[j], arr[k]))
        
    temp = []
    for nums in s:
        temp.append(nums)
        
    return temp


# Optimal
def threeSum(arr):
    arr.sort()
    s = set()
    n = len(arr)

    for i in range(n):
        low = i + 1
        high = n - 1
        while low < high:
            sum = arr[i] + arr[low] + arr[high]
            if sum == 0:
                s.add((arr[i], arr[low], arr[high]))
                low += 1
                high -= 1
            elif sum < 0:
                low += 1
            else:
                high -= 1
        
    return list(s)



# 3 Sum Closest (16)
def threeSumClosest(arr, k):
    arr.sort()
    n = len(arr)
    closeSum = arr[0] + arr[1] + arr[2]

    for i in range(n):
        low = i + 1
        high = n - 1
        while low < high:
            sum = arr[i] + arr[low] + arr[high]
            if abs(k - sum) < abs(k - closeSum):
                closeSum = sum
                
            if sum < k:
                low += 1
            else:
                high -= 1
        
    return closeSum
                




# Count Good Triplets (1534)
def countGoodTriplets(arr, a, b, c):
    cnt = 0
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                t1 = abs(arr[i] - arr[j])
                t2 = abs(arr[j] - arr[k])
                t3 = abs(arr[i] - arr[k])

                if t1 <= a and t2 <= b and t3 <= c:
                    cnt += 1
        
    return cnt
