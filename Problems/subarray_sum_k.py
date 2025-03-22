from typing import List


class SubArraySumK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        total = 0
        table = {}
        for i in range(len(nums)):
            total += nums[i]
            if total ==  k:
                counter += 1
            
            diff = total - k
            if diff in table:
                counter += table[diff]
            
            if total in table:
                table[total] += 1
            else:
                table[total] = 1
        
        return counter