from typing import List, Optional

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
    

class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PathSum:
    def hasPathSum(self, root: Optional[TreeNode2], targetSum: int) -> bool:
        def cal_sum(cur_sum, node):
            if not node:
                return False
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            
            return (cal_sum(cur_sum, node.left) or cal_sum(cur_sum, node.right))
        
        return cal_sum(0, root)
    
# class MinPathSum:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         row = len(grid)
#         col = len(grid[0])

#         cur_row = cur_col = 0
#         cur_sum = 0

#         going_right = True
#         going_down = True

#         if going_right:
#             while cur_row >= 0 and cur_col < col:
#                 cur_sum += grid[cur_row][cur_col]
                
#         for i in range(col):
#             for j in range(row):
#                 cur_sum += grid

