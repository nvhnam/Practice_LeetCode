from typing import List


class ProductArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = 1
        ans.append(prefix)
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            ans.append(prefix)
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans