# 24. Swap Nodes in Pairs
class Node:
    def Node(self, data):
        self.head = data
        self.next = None

def swapPairs(head):
    if head is None or head.next is None:
        return head
    
    dummy = Node(0)
    temp = dummy
    curr = head

    while curr and curr.next:
        temp.next = curr.next
        curr.next = temp.next.next
        temp.next.next = curr

        temp = curr
        curr = curr.next
    
    return dummy.next



# Using Recursion
def swapPairs(head):
    if head is None or head.next is None:
        return head
    
    temp = head.next

    head.next = swapPairs(head.next.next)
    temp.next = head

    return temp


# Recursion 2
def swapPairs(head):
    if head is None or head.next is None:
        return head
    
    temp = head.next
    curr = head.next.next
    temp.next = head
    head.next = swapPairs(curr)
    return temp



# 25. Reverse Nodes in k-Group
def solve(head, size, k):
    if not head or size < k:
        return head
    
    curr = head
    temp = None
    prev = None
    cnt = 0

    while curr and cnt < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        cnt += 1
    
    head.next = solve(curr, size - k, k)
    return prev


def reverseKGroup(head, k):
    size = 0
    temp = head

    while temp:
        temp = temp.next
        size += 1

    return solve(head, size, k)


# Find the size of LL
# Reverse for k groups using "reverse" code and recursively call that function for size - k.


# 2074. Reverse Nodes in Even Length Groups