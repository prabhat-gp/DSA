# 26. Remove Duplicates from Sorted Array

# Approach 1
def removeDuplicates(arr, n):
    if n == 0:
        return 0
    
    i = 0
    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1




# 27. Remove Element
def removeElement(arr, n, k):
    index = 0
    for i in range(n):
        if arr[i] != k:
            arr[index] = arr[i]
            index += 1
    
    return i




# 80. Remove Duplicates from Sorted Array II
def removeDuplicates(arr, n):
    if n <= 2:
        return n
    
    i = 0
    for j in range(2, n):
        if arr[i - 2] != arr[j]:
            arr[i] = arr[j]
            i += 1
    
    return i




# 203. Remove Linked List Elements