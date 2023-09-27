# Intersection of Two Arrays

# No duplicates in final answer
def intersection(arr1, arr2):
    s1 = set()
    s2 = set()

    for i in range(len(arr1)):
        s1.add(arr1[i])
    
    for i in range(len(arr2)):
        if arr2[i] in s1:
            s2.add(arr2[i])
    
    return s2



# Include the intersection element in final answer as many times as it is repeated
def intersection(arr1, arr2):
    map = {}
    temp = []

    for i in range(len(arr1)):
        # map[arr1[i]] = map.get(map[arr1[i], 0]) + 1
        if arr1[i] in map:
            map[arr1[i]] += 1
        else:
            map[arr1[i]] = 1
    
    for i in range(len(arr2)):
        if arr2[i] in map and map[arr2[i]] > 0:
            temp.append(arr2[i])
            map[arr2[i]] -= 1
    
    return temp


# 2 Pointer Approach
def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    temp = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            temp.append(arr1[i])
            i += 1
            j += 1
    
    return temp



# 2215. Find the Difference of Two Arrays 