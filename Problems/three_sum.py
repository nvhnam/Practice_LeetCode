from typing import List


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