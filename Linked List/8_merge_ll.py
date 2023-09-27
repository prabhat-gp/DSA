# 21. Merge Two Sorted Lists
class Node:
    def Node(self, data):
        self.head = data
        self.next = None


# Using Recursion
def mergeTwoLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data < head2.data:
        head1.next = mergeTwoLists(head1.next, head2)
        return head1
    else:
        head2.next = mergeTwoLists(head1, head2.next)
        return head2
    

# Approach 2
# Similar to 203, 2487
def mergeTwoLists(head1, head2):
    dummy = Node(0)    
    temp = dummy

    while head1 and head2:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
    
    if head1: 
        temp.next = head1
    if head2:
        temp.next = head2
    
    return dummy.next




# 23. Merge k Sorted Lists
def mergeTwoLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data < head2.data:
        head1.next = mergeTwoLists(head1.next, head2)
        return head1
    else:
        head2.next = mergeTwoLists(head1, head2.next)
        return head2
    
def mergeKLists(lists):
    if not lists:
        return None
    
    while len(lists) > 1:
        merged = mergeTwoLists(lists[0], lists[1])
        lists.pop(0)
        lists.pop(0)
        lists.append(merged)
    
    return lists[0]




# 147. Insertion Sort List

# 148. Sort List (Merge Sort)
def mergeList(head1, head2):
    dummy = Node(0)
    temp = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
    
    if head1 is not None:
        temp.next = head1

    if head2 is not None:
        temp.next = head2
    
    return dummy.next


def sortList(head):
    if head is None or head.next is None:
        return head
    
    slow = head
    fast = head
    temp = None

    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    temp.next = None

    head1 = sortList(head)
    head2 = sortList(slow)

    return mergeList(head1, head2)
