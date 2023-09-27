# 206. Reverse Linked List I
class Node:
    def Node(self, data):
        self.data = data
        self.next = None


def reverse(head):
    if head is None:
        return -1
    
    curr = head
    temp = None
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev




# 92. Reverse Linked List II (Reverse between left and right)
def reverse(head, left, right):
    if head is None or left == right:
        return head
    
    dummy = Node(0, head)
    leftPrev = dummy
    curr = head
    for i in range(left - 1):
        leftPrev = curr
        curr = curr.next
    
    prev = None
    for i in range(right - left + 1):
        tempNext = curr.next
        curr.next = prev
        prev = curr
        curr = tempNext
    
    leftPrev.next.next = curr
    leftPrev.next = prev

    return dummy.next




# 160. Intersection of Two Linked List
def intersetPoint(head1, head2):
    if head1 is None or head2 is None:
        return None
    
    ptr1 = head1
    ptr2 = head2

    while ptr1 != ptr2:
        if ptr1 is None:
            ptr1 = head2
        else:
            ptr1 = ptr1.next
        
        if ptr2 is None:
            ptr2 = head1
        else:
            ptr2 = ptr2.next
    
    if ptr1 is not None:
        return ptr1.data
    
    return -1
    




# 599. Minimum Index of Two Lists

# 430. Flatten a Multilevel Doubly Linked List