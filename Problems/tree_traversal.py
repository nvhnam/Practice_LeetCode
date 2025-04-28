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

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root