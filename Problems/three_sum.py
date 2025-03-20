from typing import List, Optional


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

class TwoSum:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        sum = 0
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            elif sum == target:
                res.append(i+1)
                res.append(j+1)
                return res

        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    

class TwoSumIV:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = set()
        def dfs(node):
            if not node:
                return False
            y = k - node.val
            if y in l:
                return True
            else:
                l.add(node.val)
                return (dfs(node.left) or dfs(node.right))
        return dfs(root)