# 141. Linked List Cycle (Detect Cycle T/F)

def hasCycle(head):
    if head is None:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False



# 142. Linked List Cycle II (Detect Node)
def detectCycle(head):
    if head is None:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None
    
    if fast != slow:
        return None
    
    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast

