# 61. Rotate Linked List

def rotateLeft(head, k):
    if not head:
        return head
    
    temp = head
    cnt = 1
    while temp.next:
        temp = temp.next
        cnt += 1
    
    temp.next = head
    k = k % cnt
    while k != 0:
        temp = temp.next
        k -= 1
    
    ptr = temp.next
    temp.next = None

    return ptr
 



def rotateRight(head, k):
    if not head:
        return head
    
    temp = head
    cnt = 1
    while temp.next:
        temp = temp.next
        cnt += 1
    
    temp.next = head
    k = cnt - (k % cnt)
    while k != 0:
        temp = temp.next
        k -= 1
    
    ptr = temp.next
    temp.next = None

    return ptr
 



# 725. Split Linked List in Parts
def splitListToParts(head, k):
    temp = head
    cnt = 0
    while temp:
        temp = temp.next
        cnt += 1
    
    base_len = cnt // k
    remainder = cnt % k
    res = [0] * k
    curr = head

    for i in range(k):
        res[i] = curr

        for j in range(base_len + (1 if remainder else 0)):
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = None
        
        if remainder > 0:
            remainder -= 1

    return res




# 328. Odd Even Linked List (Rearrange a LL)
def oddEvenList(head):
    if not head or not head.next or not head.next.next:
        return head
    
    odd = head
    even = head.next
    evenStart = head.next

    while odd.next and even.next:
        odd.next = even.next
        even.next = odd.next.next
        odd = odd.next
        even = even.next
    
    odd.next = evenStart

    return head

