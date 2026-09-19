class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        toArray(root, arr, 0)
        return arr

def toArray(node: Optional[TreeNode], arr: List[List[int]], h: int):
    if node is None: return
    if 0 <= h < len(arr):
        arr[h].append(node.val)
    else:
        arr.append([node.val])
    toArray(node.left, arr, h+1)
    toArray(node.right, arr, h+1)