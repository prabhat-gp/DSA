# 86. Partition List

class Node:
    def Node(self, data):
        self.head = data
        self.next = None


def partition(head, k):
    left = Node(0)
    right = Node(0)

    ptr1 = left
    ptr2 = right
    temp = head

    while temp:
        if temp.data < k:
            ptr1.next = temp
            ptr1 = ptr1.next
        else:
            ptr2.next = temp
            ptr2 = ptr2.next
        temp = temp.next
    
    ptr1.next = right.next
    ptr2.next = None

    return left.next
        


# 2161. Partition Array According to Given Pivot
