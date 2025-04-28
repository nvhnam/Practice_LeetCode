from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and dfs(left.left, right.right) 
                    and dfs(left.right, right.left))
        return dfs(root.left, root.right)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth = float("inf")
        self.dfs(root, 0)
        return self.min_depth

    def dfs(self, root, cur_depth):
        if not root: 
            return
        if not root.left and not root.right:
            self.min_depth = min(self.min_depth, cur_depth + 1)
        self.dfs(root.left, cur_depth + 1)
        self.dfs(root.right, cur_depth + 1) 