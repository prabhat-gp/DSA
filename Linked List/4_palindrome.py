# 234. Palindrome Linked List

# Approach 1
def isPalindrome(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = slow
    slow = slow.next
    prev.next = None

    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        

    fast = head
    slow = prev

    while slow:
        if fast.data != slow.data:
            return False
        fast = fast.next
        slow = slow.next
    
    return True




# Approach 2
def getMid(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse(head):
    curr = head
    prev = None
    temp = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def isPalindrome(head):
    if head is None:
        return None
    
    mid = getMid(head)

    temp = mid.next
    mid.next = reverse(temp)

    head1 = head
    head2 = mid.next

    while head2:
        if head1.data != head2.data:
            return False
        
        head1 = head1.next
        head2 = head2.next
    
    temp = mid.next
    mid.next = reverse(temp)
    return True




# 2130. Maximum Twin Sum of Linked List (Reverse, Middle, Palindrome)

# Approach 1
def isPalindrome(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = slow
    slow = slow.next
    prev.next = None

    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        

    fast = head
    slow = prev
    maxSum = 0

    while slow:
        maxSum = max(maxSum, slow.data + fast.data)
        fast = fast.next
        slow = slow.next
    
    return maxSum


# Approach 2
def getMid(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse(head):
    curr = head
    prev = None
    temp = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def pairSum(head):
    if head is None:
        return None
    
    mid = getMid(head)
    temp = mid.next
    mid.next = None
    temp = reverse(temp)

    maxSum = 0
    ptr1 = head
    ptr2 = temp

    while ptr1:
        maxSum = max(maxSum, ptr1.data + ptr2.data)
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    temp = reverse(temp)
    mid.next = temp

    return maxSum


    


# 143. Reorder List (Combination of Reverse a Linked List I & II)
# Approach 1
def reorderList(head):
    if head is None:
        return None
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = slow
    slow = slow.next
    prev.next = None

    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    fast = head
    slow = prev

    while slow.next:
        temp1 = fast.next
        temp2 = slow.next

        fast.next = slow
        slow.next = temp1

        fast = temp1
        slow = temp2



# Approach 2
def getMid(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse(head):
    curr = head
    prev = None
    temp = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def reorderList(head):
    if head is None:
        return None
    
    mid = getMid(head)
    reversed_head = reverse(mid.next)
    mid.next = None

    ptr1 = head
    ptr2 = reversed_head

    while ptr2:
        temp1 = ptr1.next
        temp2 = ptr2.next

        ptr1.next = ptr2
        ptr2.next = temp1

        ptr1 = temp1
        ptr2 = temp2
    
