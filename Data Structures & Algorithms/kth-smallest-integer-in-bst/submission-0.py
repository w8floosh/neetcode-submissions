class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     if root is None:
    #         return -1

    #     stack: List[TreeNode] = [root]

    #     while len(stack) != 0 or k == 0:
    #         node = stack.pop(-1)
    #         if node is None: continue

    #         if node.right: stack.append(node.right)

    #         if node.left: stack.append(node.left)
    #         else: k = k-1
        
    #     return stack.pop(-1).val
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop(-1)
        
            k = k-1
            if k == 0:
                return node.val

            node = node.right
        
        return -1


            

    

