from typing import List, Optional


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums = sorted(nums)
        print("nums: ", nums)
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                print("i: ", i)
                print("j: ", j)
                print("k: ", k)
                sum = a + nums[j] + nums[k]
                print("sum: ", sum)
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    final.append([a, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return final

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