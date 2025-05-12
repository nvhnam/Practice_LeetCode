from collections import Counter
from typing import List


class IntersectionMultipleArrays:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        c = Counter(nums[0])

        for i in range(1, len(nums)):
            for n in nums[i]:
                if n in c:
                    c[n] += 1

        res = []
        for n in c.keys():
            if c[n] == len(nums):
                res.append(n)
        return sorted(res)