from typing import List


class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            count = 1
            if(nums[i] in dict):
              val = dict.get(nums[i])
              dict.update({nums[i]: val+1})
            else:
              dict[nums[i]] = count
        max_value = max(dict.values())

        for key, value in dict.items():
           if max_value == value:
              return key
        
