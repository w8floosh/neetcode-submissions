class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = height(root)
        arr = [[] for _ in range(h)]
        toArray(root, arr, h)
        return arr

def height(node: Optional[TreeNode]) -> int:
    if node is None: return 0
    lh = height(node.left)
    rh = height(node.right)
    return 1 + max(lh, rh)

def toArray(node: Optional[TreeNode], arr: List[List[int]], h: int):
    if node is None: return
    toArray(node.left, arr, h-1)
    arr[len(arr)-h].append(node.val)
    toArray(node.right, arr, h-1)