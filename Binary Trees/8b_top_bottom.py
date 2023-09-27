# Top View of Binary Tree
import queue

def topView(root):
    if root is None:
        return []
    
    map = {}
    qu = queue.Queue()
    qu.put((root, 0))

    while not qu.empty():
        curr, temp = qu.get()
        if temp not in map:
            map[temp] = curr.data # important
        
        if curr.left:
            qu.put((curr.left, temp - 1))

        if curr.right:
            qu.put((curr.right, temp + 1))

    ans = []
    for key in sorted(map):  
        ans.append(map[key])

    return ans





# Bottom View of Binary Tree
import queue

def bottomView(root):
    if root is None:
        return []
    
    map = {}
    qu = queue.Queue()
    qu.put((root, 0))

    while not qu.empty():
        curr, temp = qu.get()
        
        map[temp] = curr.data # important
        
        if curr.left:
            qu.put((curr.left, temp - 1))

        if curr.right:
            qu.put((curr.right, temp + 1))

    ans = []
    for key in sorted(map):  
        ans.append(map[key])

    return ans



