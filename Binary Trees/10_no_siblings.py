# Print all roots that don't have sibling

def solve(root, ans):
    if root is None:
        return

    if root.left is None and root.right is not None:
        ans.append(root.right.data)

    if root.left is not None and root.right is None:
        ans.append(root.left.data)

    solve(root.left, ans)
    solve(root.right, ans)

def noSibling(root):
    ans = []
    solve(root, ans)

    if not ans:
        ans.append(-1)

    ans.sort()
    return ans

# T.C = O(NlogN) 
# S.C = O(height)