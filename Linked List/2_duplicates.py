# 83. Remove Duplicates from Sorted List (Remove the extra node)
class Node:
    def Node(self, data):
        self.data = data
        self.next = None

def deleteDuplicates(head):
    if head is None:
        return None
    
    temp = head
    while temp and temp.next:
        if temp.next.data == temp.data:
            temp.next = temp.next.next
            continue
        temp = temp.next
    
    return head

# def deleteDuplicates(head):
#     if head is None:
#         return None
    
#     curr = head
#     while curr:
#         if curr.next and curr.data == curr.next.data:
#             temp = curr.next.next
#             curr.next = None
#             curr.next = temp
#         else:
#             curr = curr.next
    
#     return head



# 82. Remove Duplicates from Sorted List II (Remove the node which is repeated completely)
# Remove all occurences of duplicates in a linked list
def deleteDuplicates(head):
    dummy = Node(-1)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        isDuplicate = False
        while curr.next and curr.data == curr.next.data:
            curr = curr.next
            isDuplicate = True
        
        if isDuplicate:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next

    return dummy.next

 

# Remove Duplicates From an Unsorted List (Remove the extra node)
def deleteDuplicates(head):
    if head is None:
        return None
    
    map = {}
    temp = head

    while temp.next:
        map[temp.data] = True

        if temp.next.data in map:
            temp.next = temp.next.next
        else:
            map[temp.data] = True
            temp = temp.next
    
    return head