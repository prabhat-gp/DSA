# 42. Trapping Rain Water

# Approach 1
def trappingWater(height, n):
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(height[i], left_max[i - 1])
    
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(height[i], right_max[i + 1])

    ans = 0
    for i in range(n):
        ans += min(left_max[i], right_max[i]) - height[i] # height[i]
    
    return ans

# T.C = O(N)
# S.C = O(N)


# Space Optimised
def trappingWater(height, n):
    low = 0
    high = n - 1
    i = 0
    j = 0
    ans = 0

    while low <= high:
        if height[low] <= height[high]:
            i = max(i, height[low])
            ans += i - height[low]
            low += 1
        elif height[low] > height[high]:
            j = max(j, height[high])
            ans += j - height[high]
            high -= 1
    
    return ans

# T.C = O(N)
# S.C = O(1)




# 11. Container with Most Water
def maxArea(height):
    low = 0
    high = n - 1
    maxi = 0

    while low < high:
        w = high - low
        h = min(height[low], height[high])
        area = h * w
        maxi = max(maxi, area)

        if height[low] < height[high]:
            low += 1
        elif height[low] > height[high]:
            high -= 1
        else:
            low += 1
            high -= 1
    
    return maxi


# 238. Product of Array Except Self
def productExceptSelf(arr, n):
    res = [1] * n

    left = 1
    for i in range(n):
        res[i] = left
        left *= arr[i]
    
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= arr[i]
    
    return res



# 152. Maximum Product Subarray
# 53. Maximum Subarray
# 198. House Robber
# 213. House Robber II
# 337. House Robber III
# 628. Maximum Product of Three Numbers
# 713. Subarray Product Less Than K
# 560. Subarray Sum Equals K