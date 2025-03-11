from typing import List


class RemoveElements:
    def remove_elements(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if(val in nums):
                nums.remove(val)
        print(nums)
        k = len(nums)
        return k