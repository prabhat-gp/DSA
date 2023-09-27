# Diagonal Traversal of binary tree
# Approach 1
import queue

def diagonal(root):
    if not root:
        return []

    q = queue.Queue()
    q.put(root)
    ans = []
    
    while not q.empty():
        temp = q.get()
        while temp:
            if temp.left:
                q.put(temp.left)
            ans.append(temp.data)
            temp = temp.right
    
    return ans

# Approach 2
def diagonal(self, root):
    diagonal_map = {}
    self.vertical_order(root, 0, diagonal_map)
    ans = []
    for hd, nodes in sorted(diagonal_map.items()):
        ans.extend(nodes)
    return ans

def vertical_order(self, root, hd, diagonal_map):
    if root is None:
        return

    if hd in diagonal_map:
        diagonal_map[hd].append(root.data)
    else:
        diagonal_map[hd] = [root.data]

    self.vertical_order(root.left, hd + 1, diagonal_map)
    self.vertical_order(root.right, hd, diagonal_map)
        