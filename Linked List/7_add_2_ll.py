# 2. Add Two Numbers
class Node:
    def Node(self, data):
        self.data = data
        self.next = None

def addTwoNumbers(head1, head2):
    h1 = head1
    h2 = head2
    temp = Node(0)
    d = temp
    sum = 0

    while h1 is not None or h2 is not None:
        sum //= 10
        if h1 is not None:
            sum += h1.data
            h1 = h1.next
        
        if h2 is not None:
            sum += h2.data
            h2 = h2.next
        
        d.next = Node(sum % 10)
        d = d.next
    
    if sum // 10 == 1:
        d.next = Node(1)
    
    return temp.next





# 445. Add Two Numbers II
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

def solve(head1, head2):
    h1 = head1
    h2 = head2
    temp = Node(0)
    d = temp
    sum = 0

    while h1 is not None or h2 is not None:
        sum //= 10
        if h1 is not None:
            sum += h1.data
            h1 = h1.next
        
        if h2 is not None:
            sum += h2.data
            h2 = h2.next
        
        d.next = Node(sum % 10)
        d = d.next
    
    if sum // 10 == 1:
        d.next = Node(1)
    
    return temp.next

def addTwoNumbers(head1, head2):
    h1 = reverse(head1)
    h2 = reverse(head2)
    temp = solve(h1, h2)

    return reverse(temp)



# 2816. Double a Number Represented as a Linked List