from typing import List


class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin_index = 0
        end_index = len(nums) - 1

        while begin_index <= end_index:
            midpoint = begin_index + (end_index - begin_index) // 2
            midpoint_value = nums[midpoint]

            if(midpoint_value == target):
                return midpoint
            
            elif(midpoint_value < target):
                begin_index = midpoint + 1
            
            else: 
                end_index = midpoint - 1
        
        if(midpoint_value < target):
            nums.insert(midpoint + 2, target)
            return midpoint + 1
        elif(midpoint_value > target):
            nums.insert(midpoint, target)
            return midpoint