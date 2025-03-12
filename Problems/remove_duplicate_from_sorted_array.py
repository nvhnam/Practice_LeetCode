from typing import List


class RemoveDuplicateFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i - 1]):
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if(nums[i] != nums[k - 2]):
                nums[k] = nums[i]
                k += 1

        print(nums)
        return k
            