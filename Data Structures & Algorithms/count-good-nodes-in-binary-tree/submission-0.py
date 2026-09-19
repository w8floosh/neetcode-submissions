class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + preorder(root.left, root.val) + preorder(root.right, root.val)

def preorder(node: Optional[TreeNode], best_good_node: int) -> int:
    if node is None: return 0
    if node.val >= best_good_node:
        return 1 + preorder(node.left, node.val) + preorder(node.right, node.val)
    else:
        return preorder(node.left, best_good_node) + preorder(node.right, best_good_node)