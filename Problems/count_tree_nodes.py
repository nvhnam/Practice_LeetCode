from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, val):
        if val == self.val:
            return 
        
        if val < self.val:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = TreeNode(val)

class CountTreeNodes:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left_depth = self.countLeftDepth(root)
        right_depth = self.countRightDepth(root)

        if(left_depth == right_depth):
            return 2**left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    
    def countLeftDepth(self, root):
        depth = 0
        while(root != None):
            root = root.left
            depth += 1
        return depth
    
    def countRightDepth(self, root):
        depth = 0
        while(root != None):
            root = root.right
            depth += 1
        return depth
    

class ValidateBinarySearchTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return (valid(node.left, left, node.val) 
            and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))