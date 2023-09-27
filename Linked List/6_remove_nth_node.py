# Delete a Node in Single Linked List
class Node:
    def Node(self, data):
        self.head = data
        self.next = None

def delNode(head, k):
    if k == 1:
        head = head.next
    else:
        temp = head
        cnt = 1
        while cnt < k - 1:
            temp = temp.next
            cnt += 1
        temp.next = temp.next.next
    
    return head



# 203. Remove Linked List Elements (Recursion)
def removeElements(head, val):
    temp = Node(0)
    temp.next = head

    curr = temp
    while curr.next:
        if curr.next.data == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
        
    return temp.next




# 237. Delete Node in a Linked List (Done but to be verified again)

# 2487. Remove Nodes From Linked List (Delete nodes having greater value on right)
# (Remove every node which has a node with a strictly greater value anywhere to the right side of it.)
# Approach 1
def delete(head):
    temp = head
    while temp and temp.next:
        if temp.data < temp.next.data:
            temp.data = temp.next.data
            temp.next = temp.next.next
            temp = head
        else:
            temp = temp.next
    
    return head



# Approach 2
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

def removeNodes(head):
    head = reverse(head)
    temp = head

    while temp and temp.next:
        if temp.data > temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    
    return reverse(head)

# Reverse, Delete Node, Next Greater Element I



# 19. Remove Nth Node From End of List
def removeNthFromEnd(head, n):
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return head
    


# Find the nth node from end of linked list
def getNthFromLast(head, n):
    slow = head
    fast = head

    for _ in range(n):
        if fast is None:
            return -1
        fast = fast.next

    if not fast:
        return head.data
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    return slow.next.data



# 2095. Delete the Middle Node of a Linked List
def deleteMiddle(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    
    temp.next = slow.next

    return head


# 876. Middle of the Linked List
def middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow






# 1721. Swapping Nodes in a Linked List
# Approach 1 (Swapped values of nodes and not pointers)
def swapNodes(head, k):
    slow = head
    fast = head
    for _ in range(1, k):
        fast = fast.next
    
    temp = fast
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    temp.data, slow.data = slow.data, temp.data
    return head


# Approach 2 (Swap pointers)