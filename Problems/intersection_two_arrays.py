from collections import Counter
from typing import List


class IntersectionTwoArrays:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)
        return list(n1 & n2)


class IntersectionTwoArraysII:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        res = []
        for n in nums2:
            if c[n] > 0:
                res.append(n)
                c[n] -= 1
        return res