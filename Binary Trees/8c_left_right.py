# Left View
# First Node in Every Level

def solve(root, ans, level):
    if root is None:
        return
    if level == len(ans):
        ans.append(root.data)
    solve(root.left, ans, level + 1)
    solve(root.right, ans, level + 1)



def LeftView(root):
    ans = []
    level = 0
    solve(root, ans, level)
    return ans



# Right View
# 

def solve(root, ans, level):
    if root is None:
        return
    if level == len(ans):
        ans.append(root.data)
    solve(root.right, ans, level + 1)
    solve(root.left, ans, level + 1)


def LeftView(root):
    ans = []
    level = 0
    solve(root, ans, level)
    return ans
